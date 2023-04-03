"""
Escreva um programa que leia números inteiros no intervalo de 0 a 50 e os armazene em um vetor com 10 posições.
Preencha um segundo vetor apenas com os números ímpares do primeiro vetor.
Imprima os dois vetores.
"""
from random import randint

numeros_inteiros = []
impares = []

while len(numeros_inteiros) < 10:
    numeros_inteiros.append(randint(0, 50))
for n in numeros_inteiros:
    if n % 2 == 1:
        impares.append(n)
print(f'Os números gerados foram: \033[32m{sorted(numeros_inteiros)}\033[m')
print(f'Os números ímpares foram: \033[32m{sorted(impares)}\033[m')
