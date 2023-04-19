"""
-> função lambda

Definição:
A função lambda é uma função (def function()) anônima.

Sintaxe:
lambda arguments : expression

O comum é armazenar a função em uma variável -> variavel = lambda x: x expression

Exemplo:
# Calcular juros de 30% sobre os preços

preco = 1000

# caso 1 - Função tradicional

def calcular_juro1(preco):
    return preco * 0.3

print(calcular_juro1((preco)))


# caso 2 - Função lambda

calcular_juro2 = lambda preco: preco * 0.3

print(calcular_juro2(preco))

>>> 300.0
>>> 300.0

Resumo: Se trata de uma outra forma de definir uma função. Ao invés de definir a função e depois chamar, a lambda
possibilita sua definição e chamada em um úncio comando (mesma linha) otimizando o código.

Obs: As funções lambda são úteis quando precisamos de uma função simples, que será utilizada apenas uma vez e não
precisa ser reutilizada em outro lugar do código.
A função lambda se faz muito útil quando é necessário chamar uma função dentro de outra função, a exemplo as funções
map(), reduce() e filter().
"""

# Exemplo1
var1 = lambda x: x + 10
print(var1(5))

print()

# Exemplo 2
# Calcular os juros de 30% para cada um dos elementos de uma lista
precos = [50, 100, 150, 300, 1000]

precos_juros = list(map(lambda x: x * 0.3, precos))
print(precos_juros)

print()

# Exemplo 3
# Checar se número é par ou impar
resultado = lambda x: f"{x} é par" if x % 2 == 0 else f"{x} é ímpar"

print(resultado(12))
print(resultado(11))
