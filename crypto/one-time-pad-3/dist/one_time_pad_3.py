import random
from secret import flag,key

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

def random_replace(origial_key):
    random_num = random.randint(0,26)
    replaced_key = ""
    for char in origial_key:
        replaced_key += chr(((ord(char) - ord('a') + random_num) % 26) + ord('a'))
    return replaced_key

position = 0
enc_flag = encrypt(flag, key, position)
position += len(flag)
print("This is the encrypted flag")
print(enc_flag)
print()
print("******************Welcome to MOCSCTF One-Time Pad Level Three!******************")
ui = ''
while len(ui) <= len(key):
    ui = input("Input your data for encrypt:").rstrip()
    replaced_key = random_replace(key)
    ciphertext = encrypt(ui, replaced_key, position)
    position += len(ui)
    if position > len(key):
        position = position % len(key)
    print("Here you are:",ciphertext)

