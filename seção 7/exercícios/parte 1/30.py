"""
Faça um programa que leia dois vetores de 10 elementos.
Crie um vetor que seja a interseção entre os 2 vetores, ou seja, que contém apenas os números que estão em
ambos os vetores. Não deve conter números repetidos.
"""
from random import randint

vetor_1 = []
vetor_2 = []

while len(vetor_1) < 10:
    vetor_1.append(randint(1, 50))
while len(vetor_2) < 10:
    vetor_2.append(randint(1, 50))
vetor_3 = set(vetor_1).intersection(set(vetor_2))
print(f'\n\t\033[32m>\033[m vetor 1 : \033[32m{vetor_1}\033[m')
print(f'\t\033[32m>\033[m vetor 2 : \033[32m{vetor_2}\033[m')
if len(vetor_3) == 0:
    print(f'\t\033[32m>\033[m Nenhum número em comum foi encontrado nois dois vetores.')
else:
    print(f'\t\033[32m>\033[m intersecção entre vetor 1 e vetor 2 : \033[32m{vetor_3}\033[m')

