"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.
"""

numeros = []
iguais = {}
cont_igual = 0
for n in range(10):
    while True:
        try:
            numeros.append(float(input(f'Digite o {n + 1}º número: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break

for n in numeros:
    if numeros.count(n) > 1:
        iguais[n] = numeros.count(n)
print(f'\nOs valores digitados foram: \033[32m{numeros}\033[m')
if len(iguais) > 0:
    print('Os valores repetidos foram, respectivamente:')
    for valor, quantidade in iguais.items():
        print(f'\t\033[32m>\033[m {valor} = {quantidade} vezes')
else:
    print(f'\t\033[32m>\033[m Nenhum valor repetido foi encontrado.')
