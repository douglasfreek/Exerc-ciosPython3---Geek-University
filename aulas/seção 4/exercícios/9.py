"""
Celsius para Kelvin -> fórmula: K = C + 273.15
"""

while True:
    try:
        celsius = int(input('Digite a temperatura em Celsius: '))
    except:
        print('\033[31merro : digite um número inteiro\033[m')
    else:
        kelvin = celsius + 273.15
        print(f'{celsius}º C convertido para Kelvin é igual a {kelvin}')
        break
