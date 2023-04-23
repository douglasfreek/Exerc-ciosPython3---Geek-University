"""
Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais.
"""
from time import sleep
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
vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
print(f'\n\033[32m>\033[m arquivo selecionado : \033[32m{arquivo}\033[m')
with open(arquivo, 'r') as file:
    sleep(1)
    print(f'\033[34m{file.read()}\033[m')
    print('\033[32mfim do arquivo\033[m'.center(50, '-'))
    print('\033[32m>\033[m Enter para continuar...')
    input()
    file.seek(0)
    print('\033[32m>\033[m vogais encontradas: ')
    print([vogal for vogal in file.read() if vogal in vogais])
    file.seek(0)
    print(f'\033[32m>\033[m Total de vogais no arquivo:'
          f' \033[32m{len([vogal for vogal in file.read() if vogal in vogais])}\033[m')