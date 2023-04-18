"""
-> map()

Definição:
A função map() executa uma função especificada para cada item em um iterável.
O item é enviado para a função como um parâmetro.

Sintaxe:
map(function, iterables)

Exemplo:
def juntar_palavras(a, b):
  return a + b

palvras = map(juntar_palavras, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(palavras))

>>> ['appleorange', 'bananalemon', 'cherrypineapple']

Resumo:
O map() edita os itens de uma lista, ou seja, uma função é aplicada em cada um dos itens
fazendo alteração em cada um deles retornando outra lista (já alterada).

Obs: A função map() pode ser facilmente substituída pelo uso de list comprehension.
"""

# Exemplo 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def dobro(valor):
    return valor * 2

var = map(dobro, numeros)
print(list(var))

print()

# Exemplo 2
import math

var1 = [1, 4, 9, 16, 25]
var2 = map(math.sqrt, var1)  # função math.sqrt retorna a raiz quadrada de um valor
print(list(var2))

print()

# Exemplo 3
precos_produtos = [899, 1000, 1099, 1999, 2500, 3650, 5000]

def aumento_preco(valor):
    if valor >= 1999:
        return valor + (valor*20)/100 # aumento de 20%

novos_precos = map(aumento_preco, precos_produtos)
print(list(novos_precos))
