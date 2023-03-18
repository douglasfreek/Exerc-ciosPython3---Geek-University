"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu aumento de 25%:
"""

while True:
    try:
        salario = float(input('Digite o salário sem o aumento proposto: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        novo_salario = salario + (salario / 100 * 25)
        print(f'O salário de R$ {salario:.2f} receberá um aumento de 25% e passará a ser R$ {novo_salario:.2f}')
        break
