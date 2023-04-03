"""
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada.
Crie um novo vetor denominado C calculando C = A - B.
Mostre na tela os dados do vetor C.
"""
from time import sleep

numeros_A = []
numeros_B = []
numeros_C = []

print('-' * 30)
print(f'{"lista A":^30}')
print('-' * 30)
for n in range(1, 11):
    while True:
        try:
            numeros_A.append(int(input(f'Digite o {n}º número inteiro: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break
print('-' * 30)
print(f'{"lista B":^30}')
print('-' * 30)
for n in range(1, 11):
    while True:
        try:
            numeros_B.append(int(input(f'Digite o {n}º número inteiro: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break
print('-' * 30)
print(f'{"gerando lista C...":^30}')
print('-' * 30)
for n, v in enumerate(numeros_A):
    numeros_C.insert(0, numeros_A[n] - numeros_B[n])
sleep(2)
numeros_C.reverse()
print(f'\t\033[32m>\033[m lista A : \033[32m{numeros_A}\033[m')
print(f'\t\t-')
print(f'\t\033[32m>\033[m lista B : \033[32m{numeros_B}\033[m')
print(f'\t\t=')
print(f'\t\033[32m>\033[m lista C : \033[32m{numeros_C}\033[m')
