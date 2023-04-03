"""
Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos
e a soma dos números positivos desse vetor.
"""
from random import randrange
from time import sleep

numeros = []
cont_negativo = 0
soma_positivo = 0

print('GERANDO LISTA COM 10 NÚMEROS ALEATÓRIOS DE -999 A 999...')
sleep(1)
print('...')
sleep(1)
print('LISTA CRIADA!')
sleep(1)

while len(numeros) < 10:
    numeros.append(randrange(-999, 999))
print(f'Lista = {numeros}')

for n in numeros:
    if n > 0:
        soma_positivo += n
    else:
        cont_negativo += 1

if cont_negativo == 0:
    print('Nenhum número negativo foi gerado!')
else:
    print(f'Foram gerados {cont_negativo} números negativos.')

print(f'A soma dos números positivos é igual a = {soma_positivo}')
