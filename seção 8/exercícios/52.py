"""
Faça uma função que receba uma matriz quadrada de ordem N e calcule sua transposta.
Se B é a matriz transposta de A então Aij = Bji
"""


def matriz(ordem):
    from random import randint
    matriz = [[randint(1, 50) for linha in range(ordem)] for num in range(ordem)]
    return matriz


def transposta(matriz_n):
    matriz_transp = []
    linha_transp = []
    for x in range(0, len(matriz_n)):
        for y in range(0, len(matriz_n)):
            linha_transp.append(matriz_n[y][x])
        matriz_transp.append(linha_transp.copy())
        linha_transp.clear()
    return matriz_transp
while True:
    try:
        ordem = int(input('\033[32m>\033[m digite a ordem da matriz: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break
matriz = matriz(ordem)
transposta = transposta(matriz)
print()
print('matriz'.center(len(matriz) * 5, '-'))
for linha in matriz:
    for num in linha:
        print(f'{num:>4}', end=' ')
    print()
print()
print('transposta'.center(len(matriz) * 5, '-'))
for linha in transposta:
    for num in linha:
        print(f'{num:>4}', end=' ')
    print()
print()

# exemplo utilizando comprehension para gerar a transposta
print([[matriz[x][y] for x, linha in enumerate(matriz)] for y, num in enumerate(matriz)])
