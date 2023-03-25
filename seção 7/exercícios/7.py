"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""

numeros = []

for n in range(10):
    while True:
        try:
            numeros.append(int(input(f'Digite o {n + 1}º número: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break

print(f'Os números digitados foram: {numeros}')
print(f'O maior número digitado foi \033[32m{max(numeros)}\033[m e seu índice é \033[32m{numeros.index(max(numeros))}'
      f'\033[m')
