"""
Polegadas para centímetros -> fórmula: C = P * 2.54
"""

while True:
    try:
        pol = float(input('Digite a medida em polegadas: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        cm = pol * 2.54
        print(f'{pol} polegadas convertido em centímetros é igual a {cm:.1f} cm.')
        break
