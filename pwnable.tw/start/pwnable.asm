
# Function intro
push esp   # function intro 
push _exit # return address??

# Register clear
xor eax, eax # Set eax to 0
xor ebx, ebx # Set ebx to 0
xor ecx, ecx # Set ecx to 0
xor edx, edx # Set edx to 0

# Print output to screen
push 0x3a465443 # ascii
push 0x20656874 # ascii
push 0x20747261 # ascii
push 0x74732073 # ascii
push 0x2774654c # ascii
# pushed 20 = 0x14 bytes to the stack
mov ecx, esp # ecx = esp
mov dl, 0x14 # edx = 0x14
mov bl, 0x1  # ebx = 0x1
mov al, 0x4  # eax = 0x4
int 0x80   # Sys call 
# eax == 4 -> sys_write
# ebx = file descriptor = 0x1 -> stdout
# ecx = *buffer = 0 ???
# edx = count = 0x14 -> len of the string

# Read input
xor ebx, ebx # ebx = 0
mov dl, 0x3c # edx = 0x3c
mov al, 0x3  # eax = 0x3
int 0x80 # Sys cal
# eax = 0x3 -> sys_read
# ebx = 0 -> file descriptor = 0 -> stdin
# ecx = esp yay stack
# edx = 0x3c -> count size of the read

# So the idea is that the input read will be stored 
# on the stack and we can overwrite the return addr
# with the one of the system call
# so "A" * 20 + system_addr > prog

# Funciton outro
add esp, 0x14 
retn
