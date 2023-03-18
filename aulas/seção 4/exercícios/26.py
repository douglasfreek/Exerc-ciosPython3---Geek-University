"""
Metros quadrados em hectares -> fórmula: H = M * 0.0001
"""

while True:
    try:
        metros_quadrados = float(input('Digite a área em metros quadrados: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        hectare = metros_quadrados * 0.0001
        print(f'{metros_quadrados} m² convertido em hectares é igual a {hectare} hectares.')
        break
