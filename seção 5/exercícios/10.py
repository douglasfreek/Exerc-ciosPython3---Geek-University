"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas:
    - Homens: (72.7 * h) - 58
    - Mulheres: (62.1 * h) - 44.7
"""

feminino = False
masculino = False

while True:
    try:
        altura = float(input('Digite a altura da pessoa: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

while True:
    try:
        sexo = str(input('Digite o sexo [ F / M ]: ')).strip().lower()[0]
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if sexo == 'f':
            feminino = True
            break
        elif sexo == 'm':
            masculino = True
            break
        else:
            print('\033[31merro : valor inválido\033[m')
            continue

if feminino:
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O peso ideal calculado é igual a {peso_ideal:.2f} Kg')
if masculino:
    peso_ideal = (72.7 * altura) - 58
    print(f'O peso ideal calculado é igual a {peso_ideal:.2f} Kg')
