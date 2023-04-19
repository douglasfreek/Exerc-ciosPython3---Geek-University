"""
Faça uma função que receba uma matriz de 3 x 3 elementos.
Calcule e retorne a soma dos elementos que estão abaixo da diagonal principal.
"""


def matriz(linha=3, coluna=3):
    matriz = []
    diagonal_menor = []
    while len(matriz) < 3:
        linha = []
        while len(linha) < 3:
            try:
                linha.append(int(input('Digite 9 números para incluir na matriz 3x3 : ')))
            except:
                print('\033[31merro : valor inválido\033[m')
                continue
        matriz.append(linha)
    for x, linha in enumerate(matriz):
        for y, num in enumerate(linha):
            if x > y:
                print(f'\033[32m{num:>4}\33[m', end=' ')
            else:
                print(f'\033[320m{num:>4}\033[m', end=' ')
        print()
    return f'\033[32m>\033[m Soma da diagonal menor = \033[32m' \
           f'{sum([num for x, linha in enumerate(matriz) for y, num in enumerate(linha) if x > y])}\033[m'


print(matriz())
