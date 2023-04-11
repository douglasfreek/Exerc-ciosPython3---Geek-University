"""
Sejam a e b os catetos de um triângul, onde a hipotenusa é obtida pela equação: hipo = √(a ** 2 + b ** 2)
Faça uma função que receba os valores de a e b e calcule o valor da hipotenusa através da equação.
"""


def hipo(a, b):
    return (a ** 2 + b ** 2) ** 0.5


hipotenusa = hipo(a=float(input('\033[32m>\033[m Valor do cateto "a" : ')),
                  b=float(input('\033[32m>\033[m Valor do cateto "b" : ')))

print(f'\033[32m>\033[m Hipotenusa : {hipotenusa:.2f}')
