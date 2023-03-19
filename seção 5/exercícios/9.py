"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário imprima que o empréstimo não foi concedido.
Caso a prestação seja menor que 20% imprima que o empréstimo foi concedido.
"""

while True:
    try:
        salario = float(input('Digite o valor do salário: R$ '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

while True:
    try:
        prestacao = float(input('Digite o valor da prestação do empréstimo: R$ '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

proporcao = prestacao / salario * 100

if proporcao > 20:
    print(f'A proporção prestação/salário é igual a {proporcao:.2f}%')
    print('Empréstimo NEGADO')
else:
    print(f'A proporção prestação/salário é igual a {proporcao:.2f}%')
    print('Empréstimo CONCEDIDO')
