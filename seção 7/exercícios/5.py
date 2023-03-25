"""
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""
numeros = []
pares = []
impares = []

for n in range(10):
    while True:
        try:
            numeros.append(float(input(f'Digite o {n + 1}º valor: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            if numeros[n] % 2 == 0:
                pares.append(numeros[n])
            else:
                impares.append(numeros[n])
            break

if len(pares) == 0:
    print('\nNenhum número par foi digitado.\n')
else:
    print(f'\n{len(pares)} números pares foram digitados: {pares}')
if len(impares) == 0:
    print('\nNenhum número ímpar foi digitado.\n')
else:
    print(f'{len(impares)} números ímpares foram digitados: {impares}')
