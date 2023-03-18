"""
Leia um número inteiro e imprima o seu antecessor e o seu sucessor:
"""
while True:
    try:
        numero_inteiro = int(input('Digite um número inteiro: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        print(f'\t>antecessor: {numero_inteiro - 1}')
        print(f'\t>número digitado: {numero_inteiro}')
        print(f'\t>sucessor: {numero_inteiro + 1}')
        break
