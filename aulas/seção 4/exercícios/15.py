"""
Radianos em graus: π = 3.14 -> fórmula: G = R * 180 / π
"""

while True:
    try:
        rad = float(input('Digite o valor do ângulo em radianos: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        graus = rad * 180 / 3.14
        print(f'{rad} radianos convertido em graus é igual a {graus:.0f} graus.')
        break
