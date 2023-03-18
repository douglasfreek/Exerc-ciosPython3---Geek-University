"""
Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""

while True:
    try:
        valor_hora = float(input('Digite o valor da hora de trabalho: R$ '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

while True:
    try:
        horas_mes = int(input('Digite quantas horas foram trabalhadas no mês: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        subtotal = valor_hora * horas_mes
        total = subtotal + (subtotal / 100 * 10)
        print(f'\t - Valor da hora = R$ {valor_hora:.2f}')
        print(f'\t - Total de horas no mês = {horas_mes}')
        print(f'\t - Subtotal = R$ {subtotal:.2f}')
        print(f'\t - Adicional (10%) = R$ {subtotal / 100 * 10:.2f}')
        print(f'\t - Total a receber = R$ {total:.2f}')
        break
