"""
Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estao abaixo da diagonal principal
"""
from random import randint

matriz = []
numeros = []
diagonal_princ = []

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
for x, linha in enumerate(matriz):
    for y, num in enumerate(linha):
        if y < x:
            numeros.append(num)
            print(f'\033[32m{num:>4}\033[m', end=' ')
        elif y == x:
            diagonal_princ.append(num)
            print(f'\033[34m{num:>4}\033[m', end=' ')
        else:
            print(f'{num:>4}', end=' ')
    print()
print('-' * 16)
print(f'\n\033[32m>\033[m Diagonal principal = \033[34m{diagonal_princ}\033[m')
print(f'\033[32m>\033[m Soma dos numeros abaixo da diagonal principal '
      f'\033[32m{numeros}\033[m = \033[32m{sum(numeros)}\033[m ')
