"""
Leia um vetor com 20 números inteiros.
Escreva os elementos do vetor eliminando elementos repetidos.
"""
from random import randrange
from time import sleep

numeros_inteiros = []

print('Gerando vinte números inteiros de 0 a 20...')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)

while len(numeros_inteiros) < 20:
    numeros_inteiros.append(randrange(0, 20))

print(f'\033[32mLista completa:\033[m {numeros_inteiros}')
print(f'\t\033[32m>\033[m {len(numeros_inteiros)} elementos.')
print(f'\033[32mLista excluindo números repetidos:\033[m {set(numeros_inteiros)}')
print(f'\t\033[32m>\033[m {len(set(numeros_inteiros))} elementos.')
