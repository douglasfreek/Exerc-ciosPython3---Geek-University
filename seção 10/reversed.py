"""
Reversed

não confundir com a função reverse() que é uma função apenas de LISTAS
"""


lista = [1, 2, 3, 4, 5, 6]
nome = 'douglas dos santos'
res = reversed(lista)

print(res)
print(type(res))

print(list(reversed(lista)))

print(tuple(reversed(lista)))

print(set(reversed(lista)))

for numero in reversed(lista):
    print(numero, end=' ')
print()
for numero in lista:
    print(numero, end=' ')
print()
print(nome)
for letra in reversed(nome):
    print(letra, end='')
print()
print(''.join(nome))
print(''.join(reversed(nome)))
print(nome)
print(nome[::-1])
