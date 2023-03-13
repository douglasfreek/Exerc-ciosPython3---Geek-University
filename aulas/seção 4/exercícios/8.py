"""
Kelvin para Celsius -> fórmula: C=K-273.15
"""

while True:
    try:
        kelvin = float(input('Digite a temperatura em Kelvin: '))
    except:
        print('erro : digite um valor válido')
    else:
        celsius = kelvin - 273.15
        print(f'{kelvin} Kelvin convertido em Celsius é igual a {celsius:.0f}ºC')
        break
