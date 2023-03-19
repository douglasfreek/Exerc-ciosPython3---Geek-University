"""
Ler um número inteiro. Se o número lido for negativo, escreva uma mensagem de número inválido.
Se o número for positivo, calcular o logarítmo deste número.
"""
from math import log

while True:
    try:
        numero = int(input('Digite um número inteiro positivo: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if numero < 0:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            print(f'Logaritmo de {numero} na base 10 = {log(numero, 10):.2f}')
            break
