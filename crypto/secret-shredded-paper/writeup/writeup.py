from pwn import *
import itertools

context.log_level = 'debug'
#r = process(['python3', 'chall.py'])
r = remote('localhost', 1337)

r.recvuntil('Shredder size: '.encode())
n = int(r.recvuntil(b'\n', drop=True).decode(), 16)


r.recvuntil('Shredded secret: '.encode())
enc_secret = r.recvuntil(b'\n', drop=True).decode().split(':')
enc_secret = [int(s, 16) for s in enc_secret]

secret_num = len(enc_secret)
for i in range(secret_num):
    enc_secret[secret_num - i - 1] = pow(2**((64 + 16) * i), 0x10001, n) * enc_secret[secret_num - i - 1] % n

payload = ':'.join(hex(c)[2:].rjust(1024 // 8 * 2, '0') for c in enc_secret)
r.sendline(payload.encode())

r.recvuntil('Reconstructed paper: '.encode())
res = int(r.recvuntil(b'\n', drop=True).decode(), 16)

res_bin = bin(res)[2:]
secret_w_weight = []
for i in range(secret_num):
    secret_w_weight.append(res_bin[::-1][(64 + 16) * i : (64 + 16) * (i+1)][::-1])
secret_w_weight = [int(sec, 2) for sec in secret_w_weight[::-1]]

possible_divisor = [list() for _ in range(secret_num)]
for i in range(secret_num):
    for d in range(1, 5):
        if secret_w_weight[i] % d == 0 and (secret_w_weight[i] // d).bit_length() <= 64:
            possible_divisor[i].append(d)
for ds in itertools.product(*possible_divisor):
    flag = b''
    if set(ds) != set(range(1, 5)): 
        continue
    for s, d in zip(secret_w_weight, ds):
        flag += (s // d).to_bytes(8, 'big') 
    if not flag.startswith(b'MOCSCTF'): 
        continue
    else:
        print("Flag:")
        print(flag.decode())
        break