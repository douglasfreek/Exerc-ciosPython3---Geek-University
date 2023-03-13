"""
m/s em km/h -> fórmula: K=M*3.6
"""

while True:
    try:
        ms = float(input('Digite a velocidade em m/s: '))
    except:
        print('erro : digite um valor válido')
    else:
        km = ms * 3.6
        print(f'{ms} m/s convertido em Km/h é igual a {km:.0f} Km/h')
        break
