"""
Litros em metros cúbicos (m³) -> fórmula: M = L / 1000
"""

while True:
    try:
        litros = float(input('Digite a quantidade em litros: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        metro_cubicos = litros / 1000
        print(f'{litros} litros convertidos em metros cúbicos é igual a {metro_cubicos:.2f} m³.')
        break
