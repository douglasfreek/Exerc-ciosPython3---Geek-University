"""
Ler um conjunto de números reais, armazenando-os em um vetor e calcular o quadrado das componentes deste vetor,
armazenando os resultados em outro vetor.
Os conjuntos tem 10 elementos cada. Imprimir todos os conjuntos.
"""

numeros = []
numeros_ao_quadrado = []

for n in range(1, 11):
    while True:
        try:
            numeros.append(float(input(f'Digite o {n}º número: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break

print(f'Os números digitados foram: {numeros}')

for n in numeros:
    numeros_ao_quadrado.append(n ** 2)

print(f'Ao quadrado: {numeros_ao_quadrado}')
