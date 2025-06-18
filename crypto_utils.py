from cryptography.fernet import Fernet

# Encrypt a message
def encrypt_message(message, key):
    return Fernet(key).encrypt(message.encode())

# Decrypt a message
def decrypt_message(token, key):
    return Fernet(key).decrypt(token).decode()
