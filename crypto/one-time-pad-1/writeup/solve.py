from pwn import *

def decrypt(ciphertext, key, start_index):
    plaintext = ''
    for i, c in enumerate(ciphertext):
        plaintext += chr((ord(c) ^ ord(key[start_index + i])) % 256)
    return plaintext
r = process(['python3', 'one_time_pad.py'])
r.recvline()

x = str(r.recvline())
x = x[3:-4]
x = x.split(", ")
flag = []
for i in x:
    flag.append(int(i))
flag_c = ''
for i in flag:
    flag_c += chr(i)

r.recvline()
r.recvline()

r.sendline(b'a'*(5000-len(flag_c)))
response = r.recvline()

r.sendline(b'a'*len(flag_c))
x = str(r.recvline())
x = x[45:-4]
x = x.split(", ")
key = []
for i in x:
    key.append(int(i))
key_c = ''
for i in key:
    key_c += chr(i)

a = "a"*45

kb = decrypt(key_c,a,0)
ans = decrypt(flag_c,kb,0)
print(ans)

r.close()
