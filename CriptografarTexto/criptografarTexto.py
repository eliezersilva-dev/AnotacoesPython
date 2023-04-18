#  pip install cryptography

from cryptography.fernet import Fernet

# criar chave simétrica
chave = Fernet.generate_key()
print(chave.decode())
print()

texto = 'Esse texto é super hiper mega secreto'  # with open('caminho')

print(texto)
print()

cifra = Fernet(chave)
texto_cifrado = cifra.encrypt(texto.encode())  # a encriptação retornará erro se o texto não estiver em bits

print(texto_cifrado.decode())  # visualizar o texto cifrado em str (decode)
print()

texto_sem_cifra = cifra.decrypt(texto_cifrado)
print(texto_sem_cifra.decode())
