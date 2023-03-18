"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

while True:
    try:
        numero = int(input('Digite um número inteiro positivo: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if numero < 0:
            print('\033[31merro : digite um número POSITIVO\033[m')
        else:
            print(f'O número digitado foi {numero}')
            break
