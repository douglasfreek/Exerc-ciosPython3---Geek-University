"""
Faça um programa que leia um número inteiro e verifique se ele é par ou ímpar:
"""

while True:
    try:
        numero = int(input('Digite um número inteiro: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if numero % 2 == 0:
            print(f'O número {numero} é PAR')
            break
        else:
            print(f'O número {numero} é ÍMPAR')
            break
