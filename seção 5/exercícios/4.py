"""
Faça um programa que leia num número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao qudrado;
    - A raiz qudrada do número digitado.
"""

while True:
    try:
        numero = int(input('Digite um número inteiro positivo ou negativo: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if numero > 0:
            print(f'Quadrado de {numero} = {numero ** 2}')
            print(f'Raiz quadrada de {numero} = {numero ** 0.5:.2f}')
            break
        else:
            print(f'Número negativo, finalizando programa.')
            break
