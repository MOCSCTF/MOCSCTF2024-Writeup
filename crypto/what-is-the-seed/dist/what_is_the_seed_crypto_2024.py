from secret import seed, magicNum
from Crypto.Util.number import getStrongPrime, isPrime
import random
import sympy

#Hints of seed
assert(magicNum == seed >> magicNum >> magicNum >> magicNum >> magicNum)
assert(isPrime(magicNum))
assert(isPrime(magicNum - 2))
assert(isPrime(magicNum + 2))

random.seed(seed)

def get_random_prime(bits):
    rand_num = random.randrange(2**(bits-1),2**bits)
    prime = sympy.nextprime(rand_num)
    return prime

p = get_random_prime(2048)
q = get_random_prime(2048)
N = p * q 
e = 65537

with open('flag.txt', 'rb') as f:
        flag = int.from_bytes(f.read(), 'big')

        c=pow(flag, e, N)
        print(f'c = {c}')
