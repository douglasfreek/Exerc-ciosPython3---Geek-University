"""
Leia um número real. Se o número for positivo imprima a raiz quadrada.
Do contrário, imprima o número ao quadrado:
"""

while True:
    try:
        numero_real = float(input('Digite um número real positivo ou negativo: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if numero_real > 0:
            print(f'Raiz quadrada de {numero_real:.2f} é igual a {numero_real ** 0.5:.2f}')
            break
        else:
            print(f'{numero_real:.2f} ao quadrado é igual a {numero_real ** 2:.2f}')
            break
