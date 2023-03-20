"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente.
Isto é, domingo se 1, segunda-feira se 2 e assim por diante.
"""

dias_da_semana = ('domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado')

while True:
    try:
        dia = int(input('Digite o número para ver o dia da semana [1 a 7] ou [0 = SAIR]: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if dia > 7 or dia < 0:
            print('\033[31merro : valor inválido\033[m')
            continue
        elif dia == 0:
            print(f'\033[31mSaindo...\033[m')
            break
        else:
            print(f'\t> \033[34m{dias_da_semana[dia - 1].title()}\033[m')
            continue
