"""
Faça uma função e um programa de teste para cálculo do volume de uma esfera.
Sendo que o raio é passado por parâmetro.
fórmula : V = 4 / 3 * π * R ** 3
π = 3.14
"""


def volume_esfera(raio):
    return 4 / 3 * 3.14 * raio ** 3


def valor_raio():
    while True:
        try:
            raio = float(input('\033[32m>\033[m Entre com a medida do raio de uma esfera: '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            return raio


raio = valor_raio()
print(f'\033[32m>\033[m O volume encontrado para R = \033[33m{raio}\033[m é igual a '
      f'V = \033[32m{volume_esfera(raio):.2f}\033[m')
