"""
Uma empresa contrata um encanador a R$ 30.00 por dia.
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida
que deverá ser paga, sabendo que são descontados 8% para imposto de renda.
"""

diaria = 30.00
ir = 100 / 8
print(f'Preço da diária do encanador = R$ {diaria}')

while True:
    try:
        dias_trabalhados = int(input('Quantos dias o encanador trabalhou? '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        subtotal = dias_trabalhados * diaria
        print(f'\t- Dias trabalhados = {dias_trabalhados}')
        print(f'\t- Preço da diária = R$ {diaria:.2f}')
        print(f'\t- Subtotal = R$ {subtotal:.2f}')
        print(f'\t- Imposto de Renda (8%) = R$ {subtotal / 100 * 8:.2f}')
        print(f'\t- Valor Total = R$ {subtotal - (subtotal / 100 * 8):.2f}')
        break
