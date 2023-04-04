"""
Leia uma matriz 4x4, imprima a matriz e retorne a localização (linha e coluna) do maior valor
"""
from random import randint

matriz = []
maior = 0
coord = ()

for x in range(4):
    linha = []
    for y in range(4):
        linha.append(randint(1, 99))
    matriz.append(linha)

for i, x in enumerate(matriz):
    for c, y in enumerate(x):
        if y > maior:
            maior = y
            coord = (i + 1, c + 1)

print(f'\n{"matriz 4 x 4":^20}\n')
for i, x in enumerate(matriz):
    for c, y in enumerate(x):
        if y == maior:
            y = '\033[32m  ' + str(y) + '\033[m'
        if c == 0:
            print(f'|{y:>4}', end='')
        elif c == 3:
            print(f'{y:>4}  |', end='')
        else:
            print(f'{y:>4}', end='')
    print('\n', end='')

print(f'\n\033[32m>\033[m O maior número gerado na matriz foi o \033[32m{maior}\033[m')
print(f'\033[32m>\033[m Sua primeira aparição foi na linha \033[32m{coord[0]}\033[m coluna \033[32m{coord[1]}\033[m')

