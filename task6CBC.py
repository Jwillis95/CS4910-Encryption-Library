from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def cbcEncryption(plaintext: str, IV: bytes, key: bytes):
    cipher = AES.new(key, AES.MODE_CBC, IV)  # Initialize AES in CBC mode
    padding_length = 16 - (len(plaintext) % 16)
    padded_plaintext = plaintext.encode('utf-8') + bytes([padding_length] * padding_length)
    ciphertext = cipher.encrypt(padded_plaintext)  # Encrypt
    
    return ciphertext