"""
metros cúbicos (m³) em litros -> fórmula: L = 1000 * M
"""

while True:
    try:
        metro_cubico = float(input('Digite a quantidade em metros cúbicos: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        litros = metro_cubico * 1000
        print(f'{metro_cubico} metros cúbicos convertido em litros é igual a {litros:.2f} litro(s)')
        break
