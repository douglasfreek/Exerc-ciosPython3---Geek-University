"""
Leia 10 números inteiros e armazene em um vetor. Em seguida esreva os elementos que são primos e suas respectivas
posições no vetor.
"""
from random import randint

vetor = []
primos = []
posicao = 0
cont = 0

while len(vetor) < 10:
    vetor.append(randint(0, 500))
print(f'\t\033[32m>\033[m O vetor criado foi : \033[32m{vetor}\033[m')
for i, n in enumerate(vetor):
    for x in range(2, n):
        if n % x == 0:
            cont += 1
    if cont == 0:
        primos.append((n, i))
    cont = 0
if len(primos) == 0:
    print(f'\t\033[32m>\033[m Nenhum número primo foi encontrado.')
if len(primos) == 1:
    print(f'\t\033[32m>\033[m O número primo encontrado no vetor foi \033[32m{primos[0][0]}\033[m no índice '
          f'\033[32m{primos[0][1]}\033[m')
if len(primos) > 1:
    print(f'\t\033[32m>\033[m Os números primos encontrados foram: ')
    for n, i in primos:
        print(f'\t\t\033[32m> {n}\033[m no índice \033[32m{i}\033[m')
