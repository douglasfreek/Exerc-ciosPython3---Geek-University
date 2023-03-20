"""
Escreva um programa que leia um número inteiro entre 1 e 12 e imprima o mês correspondente.
Janeiro se 1, fevereiro se 2 e assim por diante.
"""

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro'
         , 'dezembro')

while True:
    try:
        mes = int(input('Digite o número para ver o mês correspondente [1 a 12] ou [0 = SAIR]: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if mes > 12 or mes < 0:
            print('\033[31merro : valor inválido\033[m')
            continue
        elif mes == 0:
            print('\033[31mSaindo...\033[m')
            break
        else:
            print(f'\t> \033[34m{meses[mes - 1]}\033[m')
            continue