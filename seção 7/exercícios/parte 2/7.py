"""
Gerar e imprimir uma matriz de tamanho 10x10, onde seus elementos sao da seguinte forma:
A[i][j] = 2i + 7j - 2       if i < j
A[i][j] = 3i² - 1           if i = j
A[i][j] = 4i³ - 5j² + 1     if 1 > j
"""
from random import randint

matriz = []

while len(matriz) < 10:
    linha = []
    while len(linha) < 10:
        num = randint(1, 50)
        if num not in linha:
            linha.append(num)
    matriz.append(linha)
print('-' * 51)
print(f'{"m a t r i z  10 x 10":^51}')
print('-' * 51)
for linha in matriz:
    for j in linha:
        print(f'{j:>4}', end=' ')
    print()
print('-' * 51)
print('-' * 51)
print(f'{"m a t r i z  10 x 10":^51}')
print('-' * 51)
for c, x in enumerate(matriz):
    for i, j in enumerate(x):
        if i < j:
            j = (2 * i) + (7 * j) - 2
            print(f'{j:>4}', end=' ')
        elif i == j:
            j = (3 * i ** 2) - 1
            print(f'{j:>4}', end=' ')
        elif i > j:
            j = (4 * i ** 3) - (5 * j ** 2) + 1
            print(f'{j:>4}', end=' ')
    print()
print('-' * 51)
