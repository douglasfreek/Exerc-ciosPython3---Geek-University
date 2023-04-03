"""
Faça um programa que receba 6 números inteiros e mostre:
    - Os números pares;
    - A soma dos números pares;
    - Os números ímpares;
    - A quantidade de números ímpares.
"""
from random import randint

numeros = []
pares = []
impares = []

while len(numeros) < 6:
    numeros.append(randint(1, 1000))

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'\n\t\033[32m>\033[m NÚMEROS = \033[32m{numeros}\033[m')
print(f'\t\033[32m>\033[m PARES = \033[32m{pares}\033[m')
print(f'\t\033[32m>\033[m SOMA DOS PARES = \033[32m{sum(pares)}\033[m')
print(f'\t\033[32m>\033[m ÍMPARES = \033[32m{impares}\033[m')
print(f'\t\033[32m>\033[m QUANT ÍMPARES = \033[32m{len(impares)}\033[m')
