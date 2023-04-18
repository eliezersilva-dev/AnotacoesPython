from hashlib import sha256

# gerar hash
senha = input('Insira a senha: ')
hash_senha = sha256(senha.encode()).hexdigest()
print(hash_senha)

with open('senhaSuperSecreta.txt', 'a', encoding="utf8") as arquivo:
    arquivo.write(f'\n{hash_senha}')

# verificação de hash
senha_login = input('Para logar insira a senha: ')
verificar_hash = sha256(senha_login.encode()).hexdigest()
print(verificar_hash)

with open('senhaSuperSecreta.txt', 'r', encoding="utf8") as banco_dados:
    linhas_banco_dados = banco_dados.readlines()
    if verificar_hash in linhas_banco_dados:
        print('Acesso liberado!')
    else:
        print('Acesso negado!')
