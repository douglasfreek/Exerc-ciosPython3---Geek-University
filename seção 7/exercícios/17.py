"""
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores negativos.
"""
from random import randrange

numeros = []
negativos = []

while len(numeros) < 10:
    numeros.append(randrange(-10, 10))

print(f'Lista: {sorted(numeros)}')

for n, num in enumerate(numeros):
    if num < 0:
        negativos.append(num)
        numeros[n] = 0

print(f'Negativos: {sorted(negativos)}')
print(f'Positivos: {sorted(numeros)}')
