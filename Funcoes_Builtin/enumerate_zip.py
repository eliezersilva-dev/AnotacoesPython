"""
-> enumerate()

Definição:
A função enumerate() retorna uma tupla de dois elementos a cada iteração:
um número sequencial e um item da sequência correspondente.

Sintaxe:
enumerate(iterables)

Exemplo:
n1 = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']
n2 = enumerate(n1)
print(list(n2))
>>> [(0, 'primeiro'), (1, 'segundo'), (2, 'terceiro'), (3, 'quarto'), (4, 'quinto')]

Resumo:
enumerate() adiciona um contador a um iterável e o retorna na forma de um objeto enumerado. Este objeto enumerate pode
então ser usado diretamente em loops for ou ser convertido em uma list().

Obs: A função enumerate() percorre UM iterável. Para percorre DOIS iteráveis e retornar um como índice do outro
utiliza a função zip().

-> zip()

Definição:
A zip()função retorna um objeto zip, que é um iterador de tuplas onde o primeiro item em cada iterador passado é
emparelhado e, em seguida, o segundo item em cada iterador passado é emparelhado, etc.
Se os iteradores passado tiverem comprimentos diferentes, o iterador com menos itens decidirá o comprimento do novo
iterador.

Sintaxe:
zip(iterator1, iterator2, iterator3 ...)

Exemplo:
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = = zip(a, b)
print(list(x)
>>>[('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]

Resumo:
Com a zip() é possível trazer 2 elementos de duas listas diferentes.

"""
# Exemplo 1
# Retorna um índice com os elementos da lista
n1 = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']
n2 = enumerate(n1)
print(list(n2))

print()

# Exemplo 2
# Usando o for retorna apenas os índices
for i in enumerate(n1):
    print((i[0]))

print()


# Exemplo 3
# Retorna o índice as palavras iniciadas com 'a'
def posicoes(lista, letra='a'):
    result = []
    for j, palavra in enumerate(lista):
        if palavra.startswith(letra):  # O startswith()método retorna True se a string começar com o valor especificado,
            # caso contrário, False.
            result.append(j)
    return result


nomes = ['abc', 'hua', 'aaa', 'asdfg', 'bnm']
print(posicoes(nomes))

print()

# Exemplo 4
# Usando a função zip()
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = zip(a, b)
print(list(x))

print()

produtos = ['celular', 'televisão', 'computador', 'videogame', 'garrafa']
precos = [899, 500, 1200, 199, 6899]
produtos_precos = list(zip(produtos, precos))
print(produtos_precos)
