"""
Faça um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e menor valor.
"""

numeros = []

for n in range(5):
    while True:
        try:
            numeros.append(float(input(f'Digite o {n + 1}º valor: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break
print(f'Os valores digitados foram: {numeros}')
print(f'O maior valor digitado foi o {max(numeros)} e está na posição {numeros.index(max(numeros))}')
print(f'O menor valor digitado foi o {min(numeros)} e está na posição {numeros.index(min(numeros))}')
