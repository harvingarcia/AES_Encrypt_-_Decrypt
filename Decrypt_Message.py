import os
from Crypto.Cipher import AES
import binascii

secret_key = "0123456789abcdef"

ciphertext_hex = input("Ingrese el mensaje cifrado (en hexadecimal): ")
if len(ciphertext_hex) % 2 != 0:
    ciphertext_hex = ciphertext_hex + '0'
ciphertext = binascii.unhexlify(ciphertext_hex)

# decipher = AES.new(secret_key, AES.MODE_ECB)
# Aqui Convertimos la clave secreta en byte #
decipher = AES.new(secret_key.encode(), AES.MODE_ECB)
decrypted_message = decipher.decrypt(ciphertext).decode('utf-8')

# Elimina el relleno del mensaje descifrado
pad_length = ord(decrypted_message[-1])
decrypted_message = decrypted_message[:-pad_length]

print("Mensaje cifrado:", ciphertext)
print("Mensaje descifrado:", decrypted_message)
