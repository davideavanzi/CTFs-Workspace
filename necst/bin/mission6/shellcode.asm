
open_call = """
mov eax, 0x5
mov ebx, esp
xor ecx, ecx
xor edx, edx
int 0x80
"""

read_code = """
mov ebx, eax
mov eax, 0x3
mov ecx, esp
mov edx, 0x30
int 0x80
"""

write_code = """
mov eax, 0x4
mov ebx, 0x1
mov edx, 0x30
int 0x80
"""