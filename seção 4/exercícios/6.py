"""
Leia uma temperatura em grau Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula da conversao é F = C * (9.0 / 5.0) + 32.0
"""

while True:
    try:
        celsius = float(input('Digite a temperatura em Cº: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        far = (celsius * (9.0/5.0)) + 32
        print(f'{celsius}ºC convertido em Fahrenheit é igual a {far:.2f}')
        break
