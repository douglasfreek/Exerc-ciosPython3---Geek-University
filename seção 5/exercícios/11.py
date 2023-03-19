"""
Escreva um programa que leia um número inteiro maior que zero e devolva, na tela, a soma de todos seus algarismos.
Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1).
Se o número lido não for maior que zero, o programa terminará com alguma mensagem de número inválido.
"""

soma = 0

while True:
    try:
        numero = int(input('Digite um número inteiro positivo: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if numero < 0:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            break

for n in (str(numero)):
    soma += int(n)

print(f'A soma de todos os algarismos de {numero} é igual a {soma}')
