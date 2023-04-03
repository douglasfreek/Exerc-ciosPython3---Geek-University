"""
Faça um programa que receba do usuário um vetor com 10 posições.
Em seguida deverá ser impresso o maior e o menor elemento do vetor.
"""

numeros = []
for n in range(10):
    while True:
        try:
            numeros.append(float(input(f'Digite o {n + 1}º número: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break

print(f'\nO maior número digitado foi {max(numeros)}')
print(f'\nO menor número digitado foi {min(numeros)}')
