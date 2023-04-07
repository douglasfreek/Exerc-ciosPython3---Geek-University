"""
Gere uma matriz 4x4 com valores no intervalo de 1 a 20. Escreva um programa que transforme a matriz gerada numa
matriz triangular inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal principal.
Imprima a matriz original e a matriz transformada.
"""
from random import randint

matriz = []

while len(matriz) < 4:
    linha = []
    while len(linha) < 4:
        num = randint(1, 20)
        if num not in linha:
            linha.append(num)
    matriz.append(linha)
print('-' * 21)
print(f'{"m a t r i z   4 x 4":^21}')
print('-' * 21)
for linha in matriz:
    for num in linha:
        print(f'{num:>4}', end=' ')
    print()
print('-' * 21)
print()
print('-' * 21)
print(f'{"m a t r i z   t. i.":^21}')
print('-' * 21)
for x, linha in enumerate(matriz):
    for y, num in enumerate(linha):
        if y <= x:
            print(f'\033[32m{num:>4}\033[m', end=' ')
        else:
            num = 0
            print(f'{num:>4}', end=' ')
    print()
