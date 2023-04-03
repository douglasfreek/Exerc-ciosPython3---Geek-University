"""
Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos.
Escreva ao final a matriz obtida.
"""
matriz = []

for lin in range(5):
    linha = []
    for col in range(5):
        if lin == col:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

print('-' * 14)
print(f'{"matriz 5x5":^14}')
print('-' * 14)

for lin, v in enumerate(matriz):
    for col, n in enumerate(v):
        if lin == col:
            print(f'\033[32m{n}\033[m', end='  ')
        else:
            print(n, end='  ')
    print(end='\n')
