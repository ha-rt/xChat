from credentials import ENCRYPTION_KEY
from cryptography.fernet import Fernet

encryptor = Fernet(ENCRYPTION_KEY)

def Encrypt(string):
    return encryptor.encrypt(string.encode())