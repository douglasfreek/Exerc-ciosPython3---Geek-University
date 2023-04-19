"""
generators

- list comprehensions
- dict comprehensions
- set comprehensions

generators são as tuples comprehensions

"""
'''
nomes = ['douglas', 'duardo', 'danilo']
print(any(nome[0] == 'd' for nome in nomes))
'''
from sys import getsizeof
'''
nomes = ['douglas', 'duardo', 'danilo']

res = [nome[0] == 'd' for nome in nomes]  # nesse caso ele retorna uma lista, um iterável, pois trata-se de uma list comprehension
print(type(res))  # <class 'list'>
print(res)  # [True, True, True]
print(getsizeof(res))  # tamanho em bytes da lista res = [True, True, True]

res = (any(nome[0] == 'd' for nome in nomes))
print(type(res))  # <class 'bool'>
print(res)  # True, retorna apenas um valor True, diferente da list comprehension, pois pelo menos um nome da lista começa com 'd'

print(getsizeof('douglas'))  # tamanho em bytes da str 'douglas'
print(getsizeof(res))  # tamanho em bytes do res que é um generator
'''
# generator ocupa menos recurso em memória do que qualquer comprehension

''' ======================================================================== '''

'''
from sys import getsizeof

# gerando uma lista de números com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
print(f'list comprehension : {list_comp} bytes')

# gerando um conjunto de números com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})
print(f'set comprehension : {set_comp} bytes')

# gerando um dicionário de números com dict comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
print(f'dict comprehension : {dict_comp} bytes')

# gerando uma lista de números com generator
generator = getsizeof((x * 10 for x in range(1000)))
print(f'generator expression : {generator} bytes')
'''

gen = (n * 1 for n in range(1001))
print([n % 2 == 0 for n in gen])  # nesse caso a expressão n % 2 == 0 será uma condição
                                  # vai retornar True se o n % 2 == 0 for verdadeiro, ou seja, se n for par

gen = (n * 1 for n in range(1001))
print([n for n in gen if n % 2 == 0])  # nesse caso, com a condição colocada depois como if, vai retornar o próprio n
                                       # caso n seja par, será colocado dentro da lista que será retornada

gen = (n * 1 for n in range(1001))
for n in gen:
    print(n, end=', ')
