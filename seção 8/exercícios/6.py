"""
Faça uma função que receba 3 números inteiros como parâmetros, representando horas, minutos e segundos.
Converta-os em segundos.
"""


def convert_segundos(horas=0, minutos=0, segundos=0):
    """
    -> Converte as horas, minutos e segundos, em um valor total convertido em segundos.
    :param horas: valor inteiro para horas
    :param minutos: valor inteiro para minutos
    :param segundos: valor inteiro para segundos
    :return: soma de todos os valores convertidos em segundos.
    """
    segundos += minutos * 60
    segundos += horas * 3600
    return segundos

print('-'.center(50, '-'))
print(' time converter tabajara 1.0 '.center(50, '-'))
print('-'.center(50, '-'))
while True:
    try:
        horas = int(input('\033[32m>\033[m Valor inteiro de horas: '))
    except ValueError:
        print('\033[31merro : valor inválido\033[m')
    else:
        break
while True:
    try:
        minutos = int(input('\033[32m>\033[m Valor inteiro de minutos: '))
    except ValueError:
        print('\033[31merro : valor inválido\033[m')
    else:
        break
while True:
    try:
        segundos = int(input('\033[32m>\033[m Valor inteiro de segundos: '))
    except ValueError:
        print('\033[31merro : valor inválido\033[m')
    else:
        break
print(f'\033[32m>\033[m \033[33m{horas}\033[m horas : \033[33m{minutos}\033[m minutos : '
      f'\033[33m{segundos}\033[m segundos\n'
      f'\033[32m>\033[m é igual = \033[32m{convert_segundos(horas, minutos, segundos)}\033[m segundos.')
