"""
Faça uma função que receba uma matriz 4x4 e retorne quantos valores maiores que 10 ela possui:
"""


def cria_matriz(linhas, colunas):
    from random import randint
    matriz = [[randint(1, 30) for num in range(colunas)] for linha in range(linhas)]
    return matriz


def maior_que_dez(mat):
    numeros = [num for linha in matriz for num in linha if num > 10]
    return list(numeros)


while True:
    try:
        linha = int(input('\033[32m>\033[m Quantidade de linhas: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break
while True:
    try:
        coluna = int(input('\033[32m>\033[m Quantidade de colunas: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

matriz = cria_matriz(linha, coluna)
print('-' * coluna * 4)
for linha in matriz:
    for num in linha:
        if num > 10:
            print(f'\033[32m{num:>3}\033[m', end=' ')
        else:
            print(f'{num:>3}', end=' ')
    print()
print('-' * coluna * 4)
print()
print(f'\033[32m>\033[m Os valores maiores que dez gerados foram: {maior_que_dez(matriz)}')
