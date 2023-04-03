"""
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não são múltiplos de 7
"""
numeros = []
numero = float(0)
while len(numeros) < 100:
    if numero % 7 != 0:
        numeros.append(numero)
    numero += 1

print(numeros)
