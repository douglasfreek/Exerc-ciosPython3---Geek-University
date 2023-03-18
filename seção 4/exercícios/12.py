"""
Milhas para Km/h -> fórmula: K = M * 1.61
"""

while True:
    try:
        milhas = float(input('Digite a velocidade em Milhas por hora (mph): '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        km = milhas * 1.61
        print(f'{milhas} mph convertido em Km/h é igual a {km:.0f} Km/h')
        break
