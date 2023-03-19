"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos:
"""

numeros = []

for n in range(1, 3):
    while True:
        try:
            numeros.append(int(input(f'Digite o {n}º número inteiro: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break

if numeros[0] > numeros[1]:
    print(f'O maior número digitado foi {numeros[0]}')
    print(f'A diferença entre {numeros[0]} e {numeros[1]} é igual a {numeros[0] - numeros[1]}')
else:
    print(f'O maior número digitado foi {numeros[1]}')
    print(f'A diferença entre {numeros[1]} e {numeros[0]} é igual a {numeros[1] - numeros[0]}')
