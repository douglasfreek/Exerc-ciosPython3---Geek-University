"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro:
"""

while True:
    try:
        num_int = int(input('Digite um número inteiro: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

sucessor = (num_int * 3) + 1
antecessor = (num_int * 2) - 1
print(f'\n>número digitado: {num_int}')
print(f'\t>sucessor de seu triplo: {sucessor}')
print(f'\t>antecessor de seu dobro: {antecessor}')
print(f'\t>soma do sucessor de seu triplo com o antecessor de seu dobro ({sucessor} + {antecessor}) = 'f'{sucessor + antecessor}')
