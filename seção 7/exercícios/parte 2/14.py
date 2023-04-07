"""
Faca um programa para gerar automaticamente numeros entre 0 e 99 de uma cartela de bingo.
Sabendo que cada cartela devera conter 5 linhas de 5 numeros, gere estes dados de modo a nao ter numeros repetidos.
O programa deve exibir na tela a cartela gerada.
"""
from random import randint

cartela = []
b = []
i = []
n = []
g = []
o = []

while len(b) < 5:
    num = randint(1, 20)
    if num not in b:
        b.append(num)
b.sort()
cartela.append(b)
while len(i) < 5:
    num = randint(21, 40)
    if num not in i:
        i.append(num)
i.sort()
cartela.append(i)
while len(n) < 5:
    num = randint(41, 60)
    if num not in n:
        n.append(num)
n.sort()
cartela.append(n)
while len(g) < 5:
    num = randint(61, 80)
    if num not in g:
        g.append(num)
g.sort()
cartela.append(g)
while len(o) < 5:
    num = randint(81, 100)
    if num not in o:
        o.append(num)
o.sort()
cartela.append(o)
print('-' * 40)
print(f'{"|  B       I       N       G       O   |":^40}')
print('-' * 40)
for x, linha in enumerate(cartela):
    for y, num in enumerate(linha):
        if y == 0:
            print(f'|\033[33m{cartela[y][x]:^6}\033[m', end='| ')
        elif y > 0 or y < 4:
            print(f'\033[33m{cartela[y][x]:^6}\033[m', end='| ')
        else:
            print(f'\033[33m{cartela[y][x]:^6}\033[m|')
    print('\n', end='')
    print('-' * 40)
