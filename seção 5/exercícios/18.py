"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas básicas.
O usuário escolhe uma das opções e seu programa então pede dois valores numéricos e realiza a operação,
mostrando o resultado.
"""
from time import sleep

while True:
    print('-' * 32)
    print(f'{"CALCULADORA":^32}')
    print('-' * 32)
    print('[ 1 ] \033[34m+\033[m', ' ' * 16, '[ 2 ] \033[34m-\033[m')
    print('[ 3 ] \033[34m/\033[m', ' ' * 16, '[ 4 ] \033[34m*\033[m')
    print(f'{"[ 0 ] Sair":^32}\n')
    try:
        operacao = int(input('Digite o código da operação: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if operacao < 0 or operacao > 4:
            print('\033[31merro : valor inválido\033[m')
            continue
        elif operacao == 0:
            print('\033[31mSaindo...\033[m')
            break
        else:
            if operacao == 1:
                print('\033[34msomar > n1 + n2\033[m:')
                while True:
                    try:
                        n1 = float(input('n1 = '))
                    except:
                        print('\033[31merro : valor inválido\033[m')
                        continue
                    else:
                        break
                while True:
                    try:
                        n2 = float(input('n2 = '))
                    except:
                        print('\033[31merro : valor inválido\033[m')
                        continue
                    else:
                        total = n1 + n2
                        print(f'> {n1} \033[34m+\033[m {n2} = \033[32m{total}\033[m')
                        sleep(2)
                        break
            elif operacao == 2:
                print('\033[34msubtrair > n1 - n2\033[m')
                while True:
                    try:
                        n1 = float(input('n1 = '))
                    except:
                        print('\033[31merro : valor inválido\033[m')
                        continue
                    else:
                        break
                while True:
                    try:
                        n2 = float(input('n2 = '))
                    except:
                        print('\033[31merro : valor inválido\033[m')
                    else:
                        total = n1 - n2
                        print(f'> {n1} \033[34m-\033[m {n2} = \033[32m{total}\033[m')
                        sleep(2)
                        break
            elif operacao == 3:
                print('\033[34mdividir > n1 / n2\033[m')
                while True:
                    try:
                        n1 = float(input('n1 = '))
                    except:
                        print('\033[31merro : valor inválido\033[m')
                        continue
                    else:
                        break
                while True:
                    try:
                        n2 = float(input('n2 = '))
                    except:
                        print('\033[31merro : valor inválido\033[m')
                    else:
                        if n2 == 0:
                            print('\033[31merro : n2 não pode ser = 0\033[m')
                            continue
                        else:
                            total = n1 / n2
                            print(f'> {n1} \033[34m/\033[m {n2} = \033[32m{total}\033[m')
                            sleep(2)
                            break
            elif operacao == 4:
                print('\033[34mmultiplicar > n1 * n2\033[m')
                while True:
                    try:
                        n1 = float(input('n1 = '))
                    except:
                        print('\033[31merro : valor inválido\033[m')
                        continue
                    else:
                        break
                while True:
                    try:
                        n2 = float(input('n2 = '))
                    except:
                        print('\033[31merro : valor inválido\033[m')
                    else:
                        total = n1 * n2
                        print(f'> {n1} \033[34m*\033[m {n2} = \033[32m{total}\033[m')
                        sleep(2)
                        break
