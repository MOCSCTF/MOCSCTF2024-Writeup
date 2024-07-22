import string
import random
from secret import flag

MIN = 500
MAX = 1000

def generate_key(length):
    characters = string.ascii_letters + string.digits
    key = ''.join(random.choices(characters, k=length))
    return key

def encrypt(plaintext, key, start_index):
    c = []
    i = 0
    for p in plaintext:
        if start_index + i == len(key):
            start_index = 0
            i = 0
        c.append(ord(p) ^ (ord(key[start_index + i])) % 256)
        i += 1
    return c

key = generate_key(random.randint(MIN,MAX))

position = 0
enc_flag = encrypt(flag, key, position)
position += len(flag)
print("This is the encrypted flag")
print(enc_flag)
print()
print("******************Welcome to MOCSCTF One-Time Pad Level Two!******************")
ui = ''
while len(ui) <= len(key):
    ui = input("Input your data for encrypt:").rstrip()
    ciphertext = encrypt(ui, key, position)
    position += len(ui)
    if position > len(key):
        position = position % len(key)
    print("Here you are:",ciphertext)

