"""
Leia o tamanho do lado de um quadrado e imprima como resultado a sua área:
"""

while True:
    try:
        lado_quadrado = float(input('Digite o tamanho do lado de um quadrado: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

print(f'> Área do quadrado: {lado_quadrado * lado_quadrado:.2f} un².')
