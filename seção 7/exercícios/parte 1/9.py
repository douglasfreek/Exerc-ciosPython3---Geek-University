"""
Crie um programa que leia 6 valores inteiros pares e, em seguida, mostre na tela todos os valores lidos
em ordem inversa.
"""
numeros = []

for n in range(6):
    while True:
        try:
            numeros.append(int(input(f'Digite o {n + 1}º valor: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if numeros[n] % 2 != 0:
                numeros.pop(n)
                print('\033[31merro : digite apenas números PARES\033[m')
                continue
            else:
                break
numeros.reverse()
print(f'Os números pares digitados, em ordem reversa, foram: {numeros}')
