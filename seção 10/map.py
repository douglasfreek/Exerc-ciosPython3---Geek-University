"""
Map

Mapeamento de valores que serão parâmetros de uma função.

map(função, iterável)
função = a função que receberá os dados do iterável, um a um
iterável = lista, tupla, dicionários, de onde a função receberá os dados


FORMA COMUM
lista = [1, 2, 3, 4, 5, 6, 7]
resultado = []
for n in lista:
    resultado.append(formula(n))
print(resultado)


"""

'''
def formula(x):
    return x + 1


lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)
print(tuple(map(formula, lista)))  # nunca esquecer do cast = list, tuple, dict'''
'''!map sempre deverá receber dois parâmetros!'''
'''o map só retornará os valores gerados pela função dentro de um iterável, por isso a obrigatoriedade do cast'''

# *** obs *** map object é um objeto que não é printável, por isso o cast

'''map com lambda'''
'''
lista = [1, 2, 3, 4, 5, 6, 7]

print(list(map(lambda x: x * 2, lista)))  # a função utilizada no parâmetro do map foi uma função lambda
'''
# *** OBS *** o map object criado só pode ser utilizado uma única vez, depois disso os dados são apagados

cidades = [('maringa', 25), ('paranavai', 35), ('curitiba', 19)]
print(cidades)
print(list(map(lambda c: (c[0], 9/5 * c[1] + 32), cidades)))

# c: vai receber cada uma das tuplas dentro da lista, com dois valores, 'cidade' e temperatura
# c = ('maringa', 25)
# c[0] = 'maringa'
# c[1] = 25
# lambda c: é a entrada, vai entrar uma tupla com dois dados, e retornar o resultado da fórmula e o nome da cidade
# c: (c[0], 9/5 * c[1] + 32), cidades





