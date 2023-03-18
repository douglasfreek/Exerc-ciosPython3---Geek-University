"""
Metros quadrados (m²) em acres -> fórmula: A = M * 0.000247
"""

while True:
    try:
        metros_quadrados = float(input('Digite a área em metros quadrados: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        acres = metros_quadrados * 0.000247
        print(f'{metros_quadrados} m² convertido em acres é igual a {acres} acres.')
        break
