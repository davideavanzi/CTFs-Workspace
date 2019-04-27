from pwn import *

argv_val = ["A" for x in range(99)]
arg_val[ord("A")] = '"\0"'
arg_val[ord("B")] = '"' + "\x20\x0a\x0d" + '"'
    
stdio_val = "\x00\x0a\x00\xff"
stderr_val = "\x00\x0a\x02\xff"
env_val = {"\xde\xad\xbe\xef":"\xca\xfe\xba\xbe"}
file_val = "\0\0\0\0"

with open("\x0a", "wb") as f:
    f.write(file_val)

p = process(["input",*argv_val], env = env_val)

p.send(stdio_val)

p.stderr.send(stderr_val)



