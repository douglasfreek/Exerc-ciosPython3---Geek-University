"""
Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares:
"""
while True:
    try:
        cotacao_dolar = float(input('Digite a cotação do dólar hoje: $ 1.00 = R$ '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

while True:
    try:
        reais = float(input('Digite o valor em reais a ser convertido: R$ '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

print(f'R$ {reais:.2f} convertidos com dólar a R$ {cotacao_dolar:.2f} = \033[32m$ {reais / cotacao_dolar:.2f}\033[m')
