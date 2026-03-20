from cryptography.fernet import Fernet

# Generar una clau
key = Fernet.generate_key()
# hola sjsj
print("MI KEY ES",key) 

"""
cipher_suite = Fernet(key)
print("clau:",key)
print("")

# Encriptar les dades
data = "Hackers, hackers everywhere"
cipher_text = cipher_suite.encrypt(data.encode())
print("Encriptat:", cipher_text)
print("")

# Desencriptar les dades
plain_text = cipher_suite.decrypt(cipher_text)
print("Desencriptat:", plain_text.decode())
"""