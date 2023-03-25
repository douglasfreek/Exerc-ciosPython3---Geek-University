"""
Faça um programa que determine e mostre os cinco primeiros números múltiplos de 3,
considerando números maiores que 0
"""

numero = 1
numeros = []
while len(numeros) < 5:
    if numero % 3 == 0:
        numeros.append(numero)
    numero += 1
print(f'Os cinco primeiros números múltiplos de 3 encontrados foram: \033[34m{numeros}\033[m')
