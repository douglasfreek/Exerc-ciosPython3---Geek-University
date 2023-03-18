"""
Quilogramas em libras -> fórmula: L = K / 0.45
"""

while True:
    try:
        kg = float(input('Digite o peso em Kg: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        libras = kg / 0.45
        print(f'{kg} Kg convertido em libras é igual a {libras:.2f} libras')
        break
