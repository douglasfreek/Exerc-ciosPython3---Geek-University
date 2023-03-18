"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos:
"""

numeros = []
quadrados = []
cont = 1
soma = 0

while True:
    try:
        numeros.append(float(input(f'Digite o {cont}º número: ')))
        cont += 1
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if cont > 3:
            break

for n, numero in enumerate(numeros):
    quadrados.append(numero ** 2)
    print(f'{n + 1} = \033[32m{numero:.2f}\033[m  ->  {numero:.2f}² = \033[34m{quadrados[n]:>5.2f}\033[m')
    soma += numero ** 2

print(f'A soma dos quadrados dos três valores \033[34m{quadrados}\033[m = \033[33m{sum(quadrados):.2f}\033[m')
