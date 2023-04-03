"""
Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
"""
from random import randint

matriz = []
maiores_que_10 = []
for l in range(4):
    linha = []
    for c in range(4):
        while True:
            try:
                linha.append(1)
            except:
                print('\033[31m> erro :\033[37m valor inválido\033[m')
            else:
                break
    matriz.append(linha)

print('-' * 30)
print(f'\033[32m{"matriz 4 x 4":^30}\033[m')
print('-' * 30)
for linha in matriz:
    print(f'\t\t{linha}')
print('-' * 30)

for linha in matriz:
    for c in linha:
        if c > 10:
            maiores_que_10.append(c)

print(f'\033[32m>\033[m {len(maiores_que_10)} valores maiores que 10: \033[32m{maiores_que_10}\033[m')
