"""
Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes.
A primeira vez deve usar a estrutura de repetição for, a segunda while, e a terceira do while.
"""

for n in range(1, 102):
    if n == 101:
        print('\n')
    else:
        print(n, end=' ')

cont = 1
while cont < 101:
    print(cont, end=' ')
    cont += 1
