"""
Metros em jardas -> fórmula: J = M / 0.91
"""

while True:
    try:
        metros = float(input('Digite o comprimento em metros: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        jardas = metros / 0.91
        print(f'{metros} metros convertido em jardas é igual a {jardas:.2f} jardas.')
        break
