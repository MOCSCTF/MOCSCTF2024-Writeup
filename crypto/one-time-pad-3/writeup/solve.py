from pwn import *
from collections import Counter

def find_most_common_number(numbers):
    num_counts = Counter(numbers)
    return max(num_counts, key=num_counts.get)

def decrypt(ciphertext, key, start_index):
    plaintext = ''
    for i, c in enumerate(ciphertext):
        plaintext += chr((ord(c) ^ ord(key[start_index + i])) % 256)
    return plaintext

r = process(['python3', 'one_time_pad_3.py'])
#r = remote("34.150.35.67",30103)
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

r.sendline(b'a'*(100-len(flag_c)))
response = r.recvline()

key_num = []
for i in range(len(flag_c)):
    count_num = []
    for j in range(500):
        r.sendline(b'a'*len(flag_c))
        x = str(r.recvline())

        start_index = x.index("[")
        x = x[start_index+1:-4]
        x = x.split(", ")

        count_num.append(int(x[i]))

        r.sendline(b'a'*(100-len(flag_c)))
        response = r.recvline()
    most_num = find_most_common_number(count_num)
    print(i+1,"/",len(flag_c),"most_num=",most_num)
    key_num.append(int(most_num))

    key_c = ''
    for i in key_num:
        key_c += chr(i)

    a = "a"*len(key_c)

    kb = decrypt(key_c,a,0)
    ans = decrypt(flag_c[0:len(key_c)],kb,0)
    print(ans)
    print("--------------------")

r.close()
