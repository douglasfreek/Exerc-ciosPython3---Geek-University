"""
Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca do valor X na matriz.
Ao final deverá escrever a localização (linha e coluna) do valor, ou uma mensagem de não encontrado.
"""
from random import randint

matriz = []
lista = set()
find = False
coord = ()

while len(matriz) < 5:
    linha = []
    while len(linha) < 5:
        num = randint(0, 99)
        if num not in lista:
            linha.append(num)
            lista.add(num)
    matriz.append(linha)
print(f'\n{"matriz 5 x 5":^21}\n')

for i, x in enumerate(matriz):
    for c, y in enumerate(x):
        print(f'{y:>3}', end=' ')
    print(end='\n')

while True:
    try:
        valor_x = int(input('\nQual número inteiro deseja procurar na matriz?\n\033[32m>\033[m '))
    except:
        print('\033[31m> erro :\033[37m valor inválido\033[m')
    else:
        break

for c, x in enumerate(matriz):
    for i, y in enumerate(x):
        if y == valor_x and len(coord) == 0:
            find = True
            coord = c + 1, i + 1

if find:
    print(f'\033[32m>\033[m O número \033[32m{valor_x}\033[m está localizado na linha \033[32m{coord[0]}'
          f'\033[m coluna \033[32m{coord[1]}\033[m')
else:
    print(f'\033[32m>\033[m O número \033[32m{valor_x}\033[m não está na matriz.')
