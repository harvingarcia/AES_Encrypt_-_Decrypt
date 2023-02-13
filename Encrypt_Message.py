import os
import binascii
from Crypto.Cipher import AES

secret_key = "0123456789abcdef"

message = input("Ingrese el mensaje: ")

# Agrega relleno al mensaje
pad_length = AES.block_size - (len(message.encode('utf-8')) % AES.block_size)
message = message + chr(pad_length) * pad_length

# cipher = AES.new(secret_key, AES.MODE_ECB)
cipher = AES.new(secret_key.encode(), AES.MODE_ECB)
ciphertext = cipher.encrypt(message.encode('utf-8'))

# decipher = AES.new(secret_key, AES.MODE_ECB)
# Aqui Convertimos la clave secreta en byte #
decipher = AES.new(secret_key.encode(), AES.MODE_ECB)
decrypted_message = decipher.decrypt(ciphertext).decode('utf-8')

# Elimina el relleno del mensaje descifrado
pad_length = ord(decrypted_message[-1])
decrypted_message = decrypted_message[:-pad_length]

#Imprimimos los mensajes
print("Mensaje original:", message)
print("Mensaje cifrado:", ciphertext)
print("Mensaje descifrado:", decrypted_message)
print("Mensaje cifrado (hexadecimal):", binascii.hexlify(ciphertext).decode('utf-8'))
