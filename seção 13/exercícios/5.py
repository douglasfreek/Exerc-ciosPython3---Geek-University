"""
Faça um programa que receba do usuário um arquivo texto e um caracter.
Mostre na tela quantas vezes aquele caractere ocorre dentro do arquivo.
"""
import os


def menu():
    """
    -> cria um menu com todos os arquivos que estão na pasta atual, cada um com um número para ser selecionado.
    :return: retorna o nome do arquivo de número escolhido
    """
    print('\033[32m>\033[m selecione um arquivo na pasta : ')
    print(f'\033[32m{os.getcwd()}\033[m')
    print('\033[32m>\033[m')
    for n, file in enumerate(os.listdir()):
        print(f'\t\033[32m[{n}]\033[m - {file}')
    while True:
        try:
            op = int(input('\033[32m>\033[m opção: '))
        except:
            print('\033[31merro : opção inválida\033[m')
        else:
            if op >= len(os.listdir()) or op < 0:
                print('\033[31merro : opção inválida\033[m')
            else:
                return os.listdir()[op]


arquivo = menu()
print(f'\033[32m>\033[m arquivo selecionado : \033[32m{arquivo}\033[m')
while True:
    carac = str(input(f'\033[32m>\033[m'
                  f' digite o caractere que gostaria de procurar dentro do arquivo \033[32m{arquivo}\033[m\n> '))
    if len(carac) > 1:
        print('\033[31m> erro : digite apenas um caractere\033[m')
        continue
    else:
        break
with open(arquivo, 'r') as arquivo:
    n_carac = list(filter(lambda c: c == carac, arquivo.read()))
    arquivo.seek(0)
    for linha in arquivo.readlines():
        for letra in linha:
            if letra != carac:
                print(f'\033[34m{letra}\033[m', end='')
            else:
                print(f'\033[31m{letra}\033[m', end='')
    print()
    print('\033[32mfim do arquivo\033[m'.center(50, '-'))
    print(f'\033[32m>\033[m \033[32m{len(n_carac)}\033[m caractere(s) \033[32m"{carac}"\033[m localizado(s).')
    print('\033[32m>\033[m Enter para finalizar...', end='')
    input()
