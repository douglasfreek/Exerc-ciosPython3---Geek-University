"""
Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor zero.
Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para trás no vetor.
"""
from random import randint

numeros = []
for n in range(1, 16):
    numeros.append(randint(0, 5))
print(numeros)

while True:
    if 0 in numeros:
        numeros.remove(0)
    else:
        break

print(numeros)
