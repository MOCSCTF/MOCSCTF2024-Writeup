from pwn import *

MIN = 500
MAX = 1000

def decrypt(ciphertext, key, start_index):
    plaintext = ''
    for i, c in enumerate(ciphertext):
        plaintext += chr((ord(c) ^ ord(key[start_index + i])) % 256)
    return plaintext

r = process(['python3', 'one_time_pad_2.py'])
#r = remote("34.150.35.67",30102)
r.recvline()


x = str(r.recvline())
x = x[3:-4]
x = x.split(", ")
#print(x)
flag = []
for i in x:
    flag.append(int(i))
print("flag =",flag)
flag_c = ''
for i in flag:
    flag_c += chr(i)


r.recvline()
r.recvline()

count = 0 #計算字元偏移
for i in range(MIN,MAX+1):
    if i % 100 == 0:
        print(i)
    count += i
    for j in range(2):
        r.sendline(b'a'*(i))
        if j == 0:
            response_a = r.recvline()
        else:
            response_b = r.recvline()
    if response_a == response_b:
        break
count *= 2
count += len(flag_c)

length = i #Key的總長
occupied_char = count%length #已佔用字元長度
available_char = length - (count%length) #剩餘未用字元長度
print("佔+剩=總長,")
print(occupied_char,"+",available_char,"=",length)

x = str(response_a)
start_index = x.index("[")
x = x[start_index+1:-4]
x = x.split(", ")

r.sendline(b'a'* available_char) #把剩餘字元佔滿
x = str(r.recvline())

r.sendline(b'a'* len(flag_c))
x = str(r.recvline())
start_index = x.index("[")
x = x[start_index+1:-4]
x = x.split(", ")

key_num = []
for i in x:
    key_num.append(int(i))
key_c = ''
for i in key_num:
    key_c += chr(i)


a = "a"*len(flag_c)
kb = decrypt(key_c,a,0)
ans = decrypt(flag_c,kb,0)
print(ans)

r.close()
