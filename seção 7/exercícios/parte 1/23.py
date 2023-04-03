"""
Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles.
Os conjuntos têm 5 elementos cada.
Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar é dado por:
x1 * y1 + x2 * y2 + ... + xn * yn.
"""
numeros_1 = []
numeros_2 = []
produto_escalar = 0

print('-' * 30)
print(f'{"lista 1":^30}')
print('-' * 30)
for n in range(1, 6):
    while True:
        try:
            numeros_1.append(float(input(f'Digite o {n}º número: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break
print('-' * 30)
print(f'{"lista 2":^30}')
print('-' * 30)
for n in range(1, 6):
    while True:
        try:
            numeros_2.append(float(input(f'Digite o {n}º número: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break
print(f'\nConjunto 1 = \033[32m{numeros_1}\033[m')
print(f'Conjunto 2 = \033[32m{numeros_2}\033[m')
print(f'Produto escalar -> ', end='')
for n in range(0, 5):
    produto_escalar += numeros_1[n] * numeros_2[n]
    print(f'\033[36m{numeros_1[n]} * {numeros_2[n]}\033[m', end='')
    if n == 4:
        print(f'\033[31m = \033[32m{produto_escalar}\033[m')
    else:
        print(' \033[32m+\033[m ', end='')
