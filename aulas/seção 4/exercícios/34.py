"""
Leia o valor do raio de um círculo, calcule e imprima a área do círculo correspondente:
A área do círculo é π * raio²
π = 3.141592
"""
while True:
    try:
        raio_circulo = float(input('Digite a medida do raio de um círculo: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        area_circulo = 3.141592 * raio_circulo ** 2
        print(f'A área do círculo em questão é igual a {area_circulo}')
        break
