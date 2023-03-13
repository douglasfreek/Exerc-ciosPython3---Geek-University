"""
Teste de exercício do curso de Python 3 da Udemy
"""

inteiro = []

for x in range(1, 4):
    while True:
        try:
            inteiro.append(int(input(f'Digite o {x}º número inteiro: ')))
        except:
            print('\033[31merro : digite um número inteiro\033[m')
        else:
            break

print(f'Os valores digitados foram {inteiro} e sua soma é igual a {sum(inteiro)}.')
