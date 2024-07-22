from secret import flag, key
assert(len(key) == 5000)

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

position = 0
enc_flag = encrypt(flag, key, position)
position += len(flag)
print("This is the encrypted flag")
print(enc_flag)
print()
print("******************Welcome to MOCSCTF One-Time Pad Level One!******************")
ui = ''
while len(ui) <= len(key):
    ui = input("Input your data for encrypt:").rstrip()
    ciphertext = encrypt(ui, key, position)
    position += len(ui)
    if position > len(key):
        position = position % len(key)
    print("Here you are:",ciphertext)

