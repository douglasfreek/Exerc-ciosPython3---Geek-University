"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((base_maior + base_menor) * altura) / 2
Lembre-se: a base maior e a base menor devem ser valores maiores que zero.
"""

while True:
    try:
        base_maior = float(input('Digite o valor da BASE MAIOR (maior que 0): '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if base_maior <= 0:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            break

while True:
    try:
        base_menor = float(input('Digite o valor da BASE MENOR (maior que 0): '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if base_menor <= 0:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            break

while True:
    try:
        altura = float(input('Digite o valor da ALTURA (maior que 0): '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if altura <= 0:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            break

area_trapezio = ((base_maior + base_menor) * altura) / 2
print(f'ÁREA DO TRAPÉZIO = {area_trapezio:.2f} un²')
