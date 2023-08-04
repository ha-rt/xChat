from Encryption.Configuration import ENCRYPTION_KEY
from cryptography.fernet import Fernet

decryptor = Fernet(ENCRYPTION_KEY)

def Decrypt(string):
    return decryptor.decrypt(string)