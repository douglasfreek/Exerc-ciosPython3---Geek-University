"""
Crie uma funcao que receba como parametro um numero inteiro e devolve o seu dobro.
"""


def dobro(numero):
    return numero * 2


while True:
    try:
        num_inteiro = int(input('\033[32m>\033[m digite um numero inteiro: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        print(f'\033[32m>\033[m dobro de \033[32m{num_inteiro}\033[m = \033[32m{dobro(num_inteiro)}\033[m')
        break