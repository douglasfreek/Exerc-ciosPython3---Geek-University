"""
Leia dois vetores de inteiros x e y, cada um com 5 elementos, impedindo o usuário de informar números repetidos.
Calcule e mostre os valores resultantes para cada caso abaixo:
    - Soma entre x e y: soma de cada elemento de x com o elemento da mesma posicao em y;
    - Produto entre x e y;
    - Diferença entre x e y;
    - Interseção entre x e y;
    - União entre x e y;
"""
from time import sleep

vetor_x = []
vetor_y = []
intersec = []

print('-' * 22)
print(f'{"vetor x":^22}')
print('-' * 22)
for n in range(5):
    while True:
        try:
            numero = int(input(f'Digite o {n + 1}º número: '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if numero in vetor_x:
                print('\033[31merro : número repetido\033[m')
            else:
                vetor_x.append(numero)
                break
sleep(1)
print('-' * 22)
print(f'{"vetor y":^22}')
print('-' * 22)
for n in range(5):
    while True:
        try:
            numero = int(input(f'Digite o {n + 1}º número: '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if numero in vetor_y:
                print('\033[31merro : número repetido\033[m')
            else:
                vetor_y.append(numero)
                break
sleep(2)

print(f'\n\033[32m>\033[m vetor x = \033[32m{vetor_x}\033[m')
print(f'\033[32m>\033[m vetor y = \033[32m{vetor_y}\033[m\n')
sleep(2)

print(f'\t\033[32m>\033[m soma dos vetores (x + y)')

for i, n in enumerate(vetor_x):
    print(f'\t\t\033[32m>\033[m {vetor_x[i]} \033[32m+\033[m {vetor_y[i]} \033[32m=\033[m {vetor_x[i] + vetor_y[i]}')
sleep(2)

print(f'\n\t\033[32m>\033[m produto dos vetores (x * y)')

for i, n in enumerate(vetor_x):
    print(f'\t\t\033[32m>\033[m {vetor_x[i]} \033[32m*\033[m {vetor_y[i]} \033[32m=\033[m {vetor_x[i] * vetor_y[i]}')
sleep(2)

print(f'\n\t\033[32m>\033[m diferença entre os vetores (x - y)')

for i, n in enumerate(vetor_x):
    print(f'\t\t\033[32m>\033[m {vetor_x[i]} \033[32m-\033[m {vetor_y[i]} \033[32m=\033[m {vetor_x[i] - vetor_y[i]}')
sleep(2)

for n in vetor_x:
    if n in vetor_y:
        intersec.append(n)
if len(intersec) == 0:
    print('\n\t\033[32m>\033[m Nenhum número em comum foi encontrado')
else:
    print(f'\n\t\033[32m>\033[m Interseção de x e y : \033[32m{intersec}\033[m')

print(f'\n\t\033[32m>\033[m União dos vetores x e y (excluindo repetidos) : '
      f'\033[32m{set(vetor_x).union(vetor_y)}\033[m')
