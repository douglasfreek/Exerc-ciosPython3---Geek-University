"""
Graus para radianos -> π = 3.14 -> fórmula: R = G * π / 180
"""
while True:
    try:
        graus = int(input('Digite o valor do ângulo em graus: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        rad = graus * 3.14 / 180
        print(f'{graus} graus convertido em radianos é igual a {rad:.4f} rad.')
        break
