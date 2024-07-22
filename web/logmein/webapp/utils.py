import re
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import json
import os


def is_alphanumeric(text):
    pattern = r'^[a-zA-Z0-9]+$'
    if re.match(pattern, text):
        return True
    else:
        return False
    
def LOG(*args, **kwargs):
    print(*args, **kwargs, flush=True)


# Some cryptographic utilities
def encode(status: dict) -> str:
    try:
        plaintext = json.dumps(status).encode()
        padded = pad(plaintext, 16)
        cipher = AES.new(os.environ["AES_KEY"].encode(), AES.MODE_ECB)
        return cipher.encrypt(padded).hex()
    except Exception as s:
        LOG(s)
        return None

def decode(inp: str) -> dict:
    try:
        token = bytes.fromhex(inp)
    
        c = AES.new(os.environ["AES_KEY"].encode(), AES.MODE_ECB)
        plaintext = c.decrypt(token)
        if plaintext[-1] <= 16:
            unpadded = unpad(plaintext, 16)
        else:
            unpadded = plaintext
        user = json.loads(unpadded)

        return user
    except Exception as s:
        LOG(s)
        return None
