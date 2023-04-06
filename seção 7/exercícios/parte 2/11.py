"""
Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estao na diagonal secundaria.
"""
from random import randint

matriz = []
diagonal_sec = []

while len(matriz) < 3:
    linha = []
    while len(linha) < 3:
        num = randint(1, 50)
        if num not in linha:
            linha.append(num)
    matriz.append(linha)
print('-' * 16)
print(f'{"matriz":^17}')
print('-' * 16)
for x, linha in enumerate(matriz, -1):
    for y, num in enumerate(linha, -1):
        if y == x * - 1:
            diagonal_sec.append(num)
            print(f'\033[32m{num:>4}\033[m', end=' ')
        else:
            print(f'{num:>4}', end=' ')
    print()
print('-' * 16)
print()
diagonal_sec.reverse()
print(f'\033[32m>\033[m Soma da diagonal secundaria \033[32m{diagonal_sec}\033[m = \033[32m{sum(diagonal_sec)}\033[m')
