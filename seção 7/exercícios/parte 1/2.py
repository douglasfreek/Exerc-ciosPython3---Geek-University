"""
Crie um programa que leia 6 valores inteiros e mostre na tela os valores lidos.
"""

lista = []

while len(lista) < 6:
    try:
        lista.append(int(input('Digite um número inteiro: ')))
    except:
        print('\033[31merro : valor inválido\033[m')

print(f'Os números lidos foram {lista}')
