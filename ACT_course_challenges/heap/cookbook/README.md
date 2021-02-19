# COOKBOOK

```python

#!/usr/bin/python
from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
r = process("./cookbook")
gdb.attach(r, """
	c
	""")

#r = remote("training.jinblack.it", 2017)
input("wait")

print (r.recvuntil(b"name?\n"))
r.send(b"stefano\n")

#create receipe
print(r.recvuntil(b"[q]uit"))
r.send(b"c\n")

#new recepie
print(r.recvuntil(b"[q]uit"))
r.send(b"n\n")

#
print(r.recvuntil(b"[q]uit"))
r.send(b"n\n")

r.interactive()
```
