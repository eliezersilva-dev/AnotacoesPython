"""
-> reduce()

Definição:
A função map() agrega todos os elementos de um conjunto em um único valor.

Sintaxe:
reduce(function, iterables)

Exemplo:
var = [2, 4, 6, 8]

def soma(a, b):
    return a + b

print(reduce(soma, var))

>>> 22

Resumo:
A função reduce() será aplicada aos elementos da sequência, até que reste apenas um.

Obs: A função reduce() deixou de ser builtin e passou a estar disponível no módulo functools a partir da versão 3.0.
Para usar basta importar -> from functools import reduce
"""

# Exemplo 1
# importando a função reduce
from functools import reduce

var = [2, 4, 6, 8]

def soma(a, b):
    return a + b

print(reduce(soma, var))
