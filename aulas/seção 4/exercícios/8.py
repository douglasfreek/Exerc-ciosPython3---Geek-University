"""
Kelvin para Celsius -> fórmula: C = K - 273.15
"""

while True:
    try:
        kelvin = float(input('Digite a temperatura em Kelvin: '))
    except:
        print('\033[31merro : digite um número inteiro\033[m')
    else:
        celsius = kelvin - 273.15
        print(f'{kelvin} Kelvin convertido em Celsius é igual a {celsius:.0f}ºC')
        break
