"""
Faça uma função que receba uma matriz de 3 x 3 elementos.
Calcule a soma dos elementos que estão acima da diagonal principal.
"""


def matriz(linha=3, coluna=3):
    from random import randint
    matriz = [[randint(1, 30) for num in range(coluna)] for linha in range(linha)]
    for x, linha in enumerate(matriz):
        for y, num in enumerate(linha):
            if x < y:
                print(f'\033[32m{num:>3}\033[m', end=' ')
            else:
                print(f'{num:>3}', end=' ')
        print()
    return matriz


def soma_acima_da_diagonal(matriz):
    diagonal = [num for x, linha in enumerate(matriz) for y, num in enumerate(linha) if x < y]
    return f'\033[32m>\033[m A soma dos números acima da diagonal principal = \033[32m{sum(diagonal)}\033[m'


mat = matriz(4, 4)
print(soma_acima_da_diagonal(mat))
