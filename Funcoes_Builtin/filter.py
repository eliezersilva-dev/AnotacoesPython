"""
-> filter()

Definição:
A função filter() retorna um iterador onde os itens são filtrados através de uma função para testar se o item é
aceito ou não.

Sintaxe:
filter(function, iterable)

Exemplo:
def maior_que_zero(valor):
    return valor > 0

valores = [10, 4, -1, 3, 5, -9, -11]

maior = filter(maior_que_zero, valores)
print(list(maior))

>>> [10, 4, 3, 5]

Resumo:
Quando se quer filtrar uma lista para pegar os itens que correspondem a uma condição se usa a filter().

Obs: Outra solução é usar o 'for' mas o filter() é mais rápido.
"""

# Exemplo 1
valores = [10, 4, -1, 3, 5, -9, -11]

def maior_que_zero(valor):
    return valor > 0

maior = filter(maior_que_zero, valores)
print(list(maior))

print()

# Exemplo 2
idades = [5, 12, 17, 18, 24, 32]

def separar_adultos(idade):
    if idade < 18:
        return False
    else:
        return True

adultos = filter(separar_adultos, idades)
for x in adultos:
    print(x)
