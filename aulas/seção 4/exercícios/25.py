"""
Acres em metros quadrados -> fórmula: M = A * 4048.58
"""

while True:
    try:
        acres = float(input('Digite a área em acres: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        metros_quadrados = acres * 4048.58
        print(f'{acres} acres convertido em metros quadrados é igual a {metros_quadrados:.2f} m².')
        break
