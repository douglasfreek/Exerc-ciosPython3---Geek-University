"""
Km/h em m/s -> fórmula: M=K/3.6
"""

while True:
    try:
        kmh = int(input('Digite a velocidade em Km/h: '))
    except:
        print('erro : digite um valor válido')
    else:
        ms = kmh/3.6
        print(f'{kmh} Km/h convertido em m/s é igual a {ms:.2f} m/s')
        break
