"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista o desconto de 12%:
"""

while True:
    try:
        preco = float(input('Digite o preço do produto: R$ '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        desconto = 12 / 100
        print(f'O produto de R$ {preco:.2f} com 12% de desconto = R$ {preco - (preco * desconto):.2f}')
        break
