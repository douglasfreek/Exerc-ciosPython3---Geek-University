"""
Faça um programa que leia um vetor de 10 números. Leia um número x.
Conte os múltiplos de um número inteiro x num vetor e mostre-os na tela.
"""
from random import randint

numeros = []
multiplos = []

while True:
    try:
        multiplo = int(input('Digite um número inteiro: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

while len(numeros) < 10:
    numeros.append(randint(1, 100))

for n in numeros:
    if n % multiplo == 0:
        multiplos.append(n)

print(f'\nOs números gerados foram: \033[32m{sorted(numeros)}\033[m')

if len(multiplos) == 0:
    print(f'\033[31mNenhum\033[m número múltiplo de \033[31m{multiplo}\033[m foi encontrado!')
elif len(multiplos) == 1:
    print(f'O número múltiplo de \033[32m{multiplo}\033[m encontrado foi \033[32m{multiplos}\033[m.')
elif len(multiplos) > 1:
    print(f'Os números múltiplos de \033[32m{multiplo}\033[m encontrados foram \033[32m{multiplos}\033[m.')
