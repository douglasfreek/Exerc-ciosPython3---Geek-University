"""
Faça um programa que possua um vetor denominado A que armazene 6 números inteiros.
O programa deve executar os seguintes passos:
    - Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7
    - Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5] e mostre a soma
    - Modifique o vetor na posição 4, atribuindo o valor 100
    - Mostre na tela cada valor do vetor A, um em cada linha
"""

lista_A = []
soma = 0

lista_A.append(1)
lista_A.append(0)
lista_A.append(5)
lista_A.append(-2)
lista_A.append(-5)
lista_A.append(7)

print(f'A lista criada possui os seguintes elementos: {lista_A}.')

for n, numero in enumerate(lista_A):
    if n == 0:
        soma += numero
    elif n == 1:
        soma += numero
    elif n == 5:
        soma += numero
print(f'A soma dos índices 0, 1 e 5 é igual a {soma}.')

lista_A[4] = 100
print(f'O valor 100 foi atribúido no índice 4 -> {lista_A}')

for n in lista_A:
    print(n)
