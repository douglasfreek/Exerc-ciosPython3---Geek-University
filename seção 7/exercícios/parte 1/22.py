"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo,
nas posições pares, os valores do primeiro, e, nas posições ímpares, os valores do segundo.
"""
from random import randint

indice_1 = 0
indice_2 = 0
indice_3 = 0
vetor_1 = []
vetor_2 = []
vetor_3 = []

for n in range(10):
    vetor_1.append(randint(0, 100))
for n in range(10):
    vetor_2.append(randint(0, 100))
while len(vetor_3) < 20:
    if indice_3 % 2 == 0:
        vetor_3.insert(indice_3, vetor_1[indice_1])
        indice_1 += 1
    else:
        vetor_3.insert(indice_3, vetor_2[indice_2])
        indice_2 += 1
    indice_3 += 1
print(f'O primeiro vetor gerado foi: \033[32m{vetor_1}\033[m')
print(f'O segundo vetor gerado foi: \033[32m{vetor_2}\033[m')
print(f'O terceiro vetor gerado, com os números do 1º vetor nas posições pares, e do 2º vetor nas posições ímpares:'
      f'\n\033[32m{vetor_3}\033[m')
