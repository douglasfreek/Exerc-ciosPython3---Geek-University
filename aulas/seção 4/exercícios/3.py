"""
Teste de exercício do curso de Python 3 da Udemy
"""

inteiro = []
for x in range(1, 4):
    inteiro.append(int(input(f'Digite o {x}º número inteiro: ')))
print(f'Os valores digitados foram {inteiro} e sua soma é igual a {sum(inteiro)}.')
