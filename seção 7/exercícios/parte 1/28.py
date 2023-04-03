"""
Leia 10 números inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2.
Copie os valores ímpares de v para v1, e os valores pares de v para v2.
"""
numeros = []
pares = []
impares = []

for n in range(10):
    while True:
        try:
            numeros.append(int(input(f'Digite o {n + 1}º número: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'\t\033[32m>\033[m Os números digitados foram: \033[32m{numeros}\033[m')
print(f'\t\033[32m>\033[m ÍMPARES = \033[32m{impares}\033[m')
print(f'\t\033[32m>\033[m PARES = \033[32m{pares}\033[m')
