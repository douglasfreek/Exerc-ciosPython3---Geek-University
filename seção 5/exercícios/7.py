"""
Faça um programa que receba dois números e mostre o maior.
Se por acaso, os dois números forem iguais, imprima uma mensagem de que os números são iguais:
"""

numeros = []

for n in range(1, 3):
    while True:
        try:
            numeros.append(int(input(f'Digite o {n}º número: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break

if numeros[0] > numeros[1]:
    print(f'O maior número digitado foi o {numeros[0]}')
elif numeros[1] > numeros[0]:
    print(f'O maior número digitado foi o {numeros[1]}')
else:
    print('Os números são iguais')
