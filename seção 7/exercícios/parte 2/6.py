"""
Leia duas matrizes 4x4 e escreva uma terceira com os maiores valores de cada posicao das matrizes lidas.
"""
from random import randint

matriz_1 = []
matriz_2 = []
matriz_maior = [[], [], [], []]

while len(matriz_1) < 4:
    linha = []
    while len(linha) < 4:
        num = randint(1, 99)
        if num not in linha:
            linha.append(num)
    matriz_1.append(linha)
while len(matriz_2) < 4:
    linha = []
    while len(linha) < 4:
        num = randint(1, 99)
        if num not in linha:
            linha.append(num)
    matriz_2.append(linha)
for l, x in enumerate(matriz_1):
    for c, y in enumerate(x):
        if y > matriz_2[l][c]:
            matriz_maior[l].append(y)
        else:
            matriz_maior[l].append(matriz_2[l][c])
print('-' * 21)
print(f'{"matriz_1  4 x 4":^21}')
print('-' * 21)
for l, x in enumerate(matriz_1):
    for c, y in enumerate(x):
        if y > matriz_2[l][c]:
            print(f'\033[32m{y:>4}\033[m', end=' ')
        else:
            print(f'{y:>4}', end=' ')
    print()
print()
print('-' * 21)
print(f'{"matriz_2  4 x 4":^21}')
print('-' * 21)
for l, x in enumerate(matriz_2):
    for c, y in enumerate(x):
        if y > matriz_1[l][c]:
            print(f'\033[32m{y:>4}\033[m', end=' ')
        else:
            print(f'{y:>4}', end=' ')
    print()
print()
print('-' * 21)
print(f'{"matriz_maior  4 x 4":^21}')
print('-' * 21)
for x in matriz_maior:
    for y in x:
        print(f'\033[32m{y:>4}\033[m', end=' ')
    print()
