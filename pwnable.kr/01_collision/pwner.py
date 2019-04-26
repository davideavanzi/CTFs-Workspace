
def hash(buffer):
	return sum((ord(c) for c in buffer)) & 0xff

import string
from itertools import product

chars = string.digits + string.letters # chars to look for


to_attempt = product(chars, repeat=5)

coll = []

for value in reversed([0x20,0xDB,0x08,0xEC]):
	for attempt in to_attempt:
        	s = ''.join(attempt)
		h = hash(s)
		if h == value:
			print("[%s]"%s)
			coll.append(list(s))
			break

result = "".join((coll[j][i] for i in range(5) for j in range(4)))
print("[%s]"%result)

from pwn import *

context.log_level = "critical"

p = process(["collisioner", result])
print(p.recvall())
