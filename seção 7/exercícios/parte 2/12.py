"""
Leia uma matriz de 3x3 elementos. Calcule e imprima sua transposta.
"""
from random import randint

matriz = []
matriz_transp = []
linha_transp = []
indice = 0

while len(matriz) < 3:
    linha = []
    while len(linha) < 3:
        num = randint(1, 10)
        if num not in linha:
            linha.append(num)
    matriz.append(linha)
print('-' * 18)
print(f'{"m a t r i z  3 x 3":^18}')
print('-' * 18)
for x, linha in enumerate(matriz):
    for num in linha:
        if x == 0:
            print(f'\033[32m{num:>4}\033[m', end=' ')
        elif x == 1:
            print(f'\033[33m{num:>4}\033[m', end=' ')
        elif x == 2:
            print(f'\033[34m{num:>4}\033[m', end=' ')
    print()
print('-' * 18)
print()
for x in range(0, 3):
    for y in range(0, 3):
        linha_transp.append(matriz[y][x])
    matriz_transp.append(linha_transp.copy())
    linha_transp.clear()
print('-' * 18)
print(f'{" m a t r i z  T":^18}')
print('-' * 18)
for linha in matriz_transp:
    for x, num in enumerate(linha):
        if x == 0:
            print(f'\033[32m{num:>4}\033[m', end=' ')
        elif x == 1:
            print(f'\033[33m{num:>4}\033[m', end=' ')
        elif x == 2:
            print(f'\033[34m{num:>4}\033[m', end=' ')
    print()
print('-' * 18)
