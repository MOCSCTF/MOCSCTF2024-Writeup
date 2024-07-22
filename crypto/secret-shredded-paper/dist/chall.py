from Crypto.Util.number import getPrime
from Crypto.Util.Padding import pad
import signal
import os
import random
import sys

def tle_handler(*args):
    print('Ojou-sama, It\'s time to go to bed')
    sys.exit(0)

class RSA:
    def __init__(self, n = 1024):
        p = getPrime(n // 2)
        q = getPrime(n // 2)
        self.n = p * q
        self.e = 0x10001
        self.d = pow(self.e, -1, (p - 1) * (q - 1))
    
    def encrypt(self, m):
        return pow(m, self.e, self.n)
    
    def decrypt(self, c):
        return pow(c, self.d, self.n)

def reconstruction(c1, c2, n):
    assert len(c1) == len(c2)
    return sum(i * j for i, j in zip(c1, c2)) % n

def main():

    signal.signal(signal.SIGALRM, tle_handler)
    signal.alarm(120) # After 60 seconds, the server will be closed
    
    FLAG = open("FLAG.txt", "rb").read()

    secret = [FLAG[i*8:(i+1)*8] for i in range(4)]
    
    rsa = RSA()
    print(f'Shredder size: {hex(rsa.n)[2:]}')

    enc_secret = []
    for block in secret:
        enc_secret.append(rsa.encrypt(int.from_bytes(block, 'big')))
    shredded_s = ':'.join(hex(c)[2:].rjust(1024 // 8 * 2, '0') for c in enc_secret)
    print(f'Shredded secret: {shredded_s}')


    ct = input('Shredded Paper, Please: ').strip().replace('-', '').split(':') # lol you can't send negative values of "paper"
    pt = [rsa.decrypt(int(c, 16)) for c in ct]

    glue_weights = list(range(1, 5))
    random.shuffle(glue_weights) # You can't balance the distribution of glue :(

    res = reconstruction(pt, glue_weights, rsa.n)
    print(f'Reconstructed paper: {hex(res)[2:]}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print('Yare yare...')