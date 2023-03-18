"""
Centímetros em polegadas -> fórmula: P = C / 2.54
"""

while True:
    try:
        cm = float(input('Digite a medida em centímetros: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        pol = cm / 2.54
        print(f'{cm:.2f} centímetros convertido em polegadas é igual a {pol:.2f} polegadas.')
        break