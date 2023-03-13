"""
Km/h para milhas -> fórmula: M = K / 1.61
"""

while True:
    try:
        km = int(input('Digite a velocidade em Km/h: '))
    except:
        print('\033[31merro : digite um número inteiro\033[m')
    else:
        milhas = km / 1.61
        print(f'{km} Km/h convertido em mph é igual a {milhas:.0f} mph')
        break
