"""
Faça uma função que receba uma matriz de 3x3 elementos.
Calcule e retorne a soma dos elementos que estão na diagonal principal.
"""


def matriz(linhas=3, colunas=3, retornar=True):
    from random import randint
    matriz = []
    while len(matriz) < linhas:
        linha = []
        while len(linha) < colunas:
            [linha.append(randint(1, 30)) for num in range(colunas)]
        matriz.append(linha)
    for x, linha in enumerate(matriz):
        for y, num in enumerate(linha):
            if x == y:
                print(f'\033[32m{num:>4}\033[m', end=' ')
            else:
                print(f'{num:>4}', end=' ')
        print()
    if retornar:
        return f'\n\033[32m>\033[m A soma dos números da diagonal principal = ' \
               f'\033[32m{sum([num for x, linha in enumerate(matriz) for y, num in enumerate(linha) if x == y])}\033[m'


print(matriz())
