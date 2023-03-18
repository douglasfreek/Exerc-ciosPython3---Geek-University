"""
Jardas em metros -> fórmula: M = 0.91 * J
"""

while True:
    try:
        jardas = float(input('Digite o comprimento em jardas: '))
    except:
        metros = 0.91 * jardas
        print(f'{jardas} jardas convertido em metros é igual a {metros:.2f} m.')
        break
