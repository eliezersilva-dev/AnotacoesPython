"""
-> list comprehension

Definição:
List comprehension é uma forma concisa de criar e manipular listas.

Sintaxe:
newlist = [expression for item in iterable if condition == True]

Exemplo:
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = [i for i in valores if i % 2 == 0]
print(par)
>>>[2, 4, 6, 8, 10]

Resumo:
Em outras palavras, aplique a expressão em cada item da lista. A condição a ser atendida é opcional, podendo inclusive
ser usados mais de uma condicional.

Obs: A list comprehension substitui de forma eficente o uso do for.
O valor de retorno de uma list comprehension é uma nova lista, deixando a lista antiga inalterada.
"""

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
palavras = ['chocolate', 'bicicleta', 'canavial', 'Demagorgon', 'ratoeira']

# Exemplo 1
dobro = [i * 2 for i in valores]
print(dobro)

print()

# Exemplo 2
par = [i for i in valores if i % 2 == 0]
print(par)

print()

# Exemplo 3
maiusculas = [i.upper() for i in palavras]
print(maiusculas)

print()

# Exemplo 4
inicia_com_c = [i for i in palavras if i.startswith('c')]
print(inicia_com_c)

print()

# Exemplo 5
indices_palavras = [i for i, j in enumerate(palavras)]
print(list(indices_palavras))



