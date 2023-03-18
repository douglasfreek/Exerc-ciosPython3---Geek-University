"""
Hectares em metros quadrados -> fórmula: M = H * 10000
"""

while True:
    try:
        hectares = float(input('Digite a área em hectares: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        metros_quadrados = hectares * 10000
        print(f'{hectares} hectares convertidos em metros quadrados é igual a {metros_quadrados:.2f} m².')
        break
