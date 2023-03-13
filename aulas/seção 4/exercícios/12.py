"""
Milhas para Km/h -> fórmula: K=M*1.61
"""

while True:
    try:
        milhas = int(input('Digite a velocidade em Milhas por hora (mph): '))
    except:
        print('erro : digite um valor válido')
    else:
        km = milhas * 1.61
        print(f'{milhas} mph convertido em Km/h é igual a {km:.0f} Km/h')
        break
