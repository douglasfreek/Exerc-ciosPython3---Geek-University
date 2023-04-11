"""Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * ((6 / 5) + 32)
"""


def convert_fahren():
    while True:
        try:
            celsius = int(input('\033[32m>\033[m Entre com a temperatura em Celsius: '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            return f'\033[32m>\033[m {celsius} graus Celsius convertidos em F = \033[32m{(celsius * 9 / 5) + 32}'\
                   f'\033[m\033[33m Fahrenheit.\033[m'
            

print(convert_fahren())
