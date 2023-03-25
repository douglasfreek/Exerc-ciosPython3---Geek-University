"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y
quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores
encontrados nas respectivas posições X e Y.
"""

numeros = []

for n in range(10):
    while True:
        try:
            numeros.append(float(input(f'Digite o {n + 1}º valor: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break
print(numeros)

while True:
    try:
        indice = int(input('Digite o nº do índice a ser mostrado [999 - Sair]: '))
    except:
        print('\033[31merro : valor inválido\033[m')
        continue
    else:
        if indice == 999:
            break
        elif indice >= len(numeros):
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            print(f'O índice escolhido foi {indice} e o seu valor é {numeros[indice]}')
            continue
