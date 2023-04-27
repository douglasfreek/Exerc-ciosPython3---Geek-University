"""
Faça uma função que receba uma matriz de 3x3 elementos.
Calcule e retorne a soma dos elementos que estão na diagonal secundária.
"""


def matriz(linha=3, coluna=3, retornar=True):
    from random import randint
    matriz = [[randint(1, 30) for num in range(coluna)] for linha in range(linha)]
    for x, linha in enumerate(matriz, -1):
        for y, num in enumerate(linha, -1):
            if x == y * - 1:
                print(f'\033[32m{num:>4}\033[m', end=' ')
            else:
                print(f'{num:>4}', end=' ')
        print()
    if retornar:
        return f'\n\033[32m>\033[m A soma dos números na diagonal secundária é = \033[32m'\
               f'{sum([num for x, linha in enumerate(matriz, -1) for y, num in enumerate(linha, -1) if x == y * - 1])}'\
               f'\033[m'
    else:
        return ''


print(matriz())
