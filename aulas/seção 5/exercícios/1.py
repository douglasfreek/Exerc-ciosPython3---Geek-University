"""
Faça um programa que receba dois números e mostre qual deles é o maior
"""
numeros = []

for n in range(1, 3):
    while True:
        try:
            numeros.append(int(input(f'Digite o {n}º número inteiro: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break
print(f'O maior número digitado foi {max(numeros)}')
