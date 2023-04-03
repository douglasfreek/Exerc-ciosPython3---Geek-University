"""
Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números,
onde m é a média do vetor.
fórmula: desvio_padrao = √ ((soma(v[i] - media)²) / n)
"""
from random import randrange
vetor = []
desvio_padrao = 0
while len(vetor) < 10:
    vetor.append(randrange(1, 100))
media = sum(vetor) / len(vetor)
print(f'\n\t\033[32m>\033[m vetor criado  : \033[32m{sorted(vetor)}\033[m')
for n in vetor:
    desvio_padrao += (n - media) ** 2
desvio_padrao = desvio_padrao / len(vetor)
desvio_padrao = desvio_padrao ** 0.5
print(f'\t\033[32m>\033[m desvio padrão : \033[32m{desvio_padrao}\033[m')
