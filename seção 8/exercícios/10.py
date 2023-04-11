"""
Faça uma função que receba dois números e retorne qual deles é o maior.
"""


def maior(x, y):
    if x == y:
        return f'{x} = {y}'
    else:
        return x if x > y else y


print(maior(x=float(input('\033[32m>\033[m Valor de x : ')), y=float(input('\033[32m>\033[m Valor de y : '))))
