"""
Libras em quilogramas -> fórmula: K = L * 0.45
"""

while True:
    try:
        libras = float(input('Digite o peso em libras: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        kg = libras * 0.45
        print(f'{libras:.2f} libras convertido em quilogramas é igual a {kg:.2f} Kg.')
        break