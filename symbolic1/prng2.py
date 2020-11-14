#!/usr/bin/python
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
r = remote("training.jinblack.it", 2020)


r.interactive()