"""
Faca uma funcao para verificar se um numero e um quadrado perfeito.
Um quadrado perfeito e um numero inteiro nao negativo que pode ser expresso como o quadrado de outro numero inteiro.
ex: 1, 4, 9...
"""


def quadrado_perfeito(numero):
    raiz = numero ** 0.5
    if raiz % 1 == 0:
        return f'\033[32m{numero}\033[33m é\033[m um quadrado perfeito. '
    else:
        return f'\033[32m{numero}\033[31m não é\033[m um quadrado perfeito.'


while True:
    try:
        num = int(input('\033[32m>\033[m Digite um número para saber se ele é um quadrado perfeito [0 - sair]: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if num == 0:
            print('\033[31m> exit <\033[m')
            break
        elif num < 0:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            print(f'\033[32m>\033[m {quadrado_perfeito(num)}')
