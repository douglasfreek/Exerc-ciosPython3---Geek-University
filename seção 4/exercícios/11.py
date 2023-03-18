"""
m/s em km/h -> fórmula: K = M * 3.6
"""

while True:
    try:
        ms = float(input('Digite a velocidade em m/s: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        km = ms * 3.6
        print(f'{ms} m/s convertido em Km/h é igual a {km:.0f} Km/h')
        break
