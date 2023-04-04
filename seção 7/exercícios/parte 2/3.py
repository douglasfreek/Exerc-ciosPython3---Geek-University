"""
Faça um programa que preencha uma matriz 4x4 com o produto do valor da linha e da coluna de cada elemento.
Em seguida imprima na tela a matriz.
"""
matriz = []

for lin in range(4):
    linha = []
    for c in range(4):
        linha.append(lin * c)
    matriz.append(linha)

for linha in matriz:
    print(linha)
