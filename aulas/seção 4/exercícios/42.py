"""
Receba o salário base de um funcionário.
Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário base.
Além disso, ele paga 7% de imposto sobre o salário base.
"""

while True:
    try:
        salario_base = float(input('Digite o salário-base: R$ '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

gratificacao = salario_base / 100 * 5
imposto = salario_base / 100 * 7

print(f'\t- Salário-base = R$ {salario_base:.2f}')
print(f'\t- Gratificação (5%) = R$ {gratificacao:.2f}')
print(f'\t- Imposto (7%) = R$ {imposto:.2f}')
print(f'\t- Salário líquido = R$ {salario_base - imposto + gratificacao:.2f}')
