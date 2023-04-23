"""
Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais
e quantas são consoantes.
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
consoantes = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
print(f'\n\033[32m>\033[m arquivo selecionado : \033[32m{arquivo}\033[m')
with open(arquivo, 'r') as file:
    sleep(1)
    print(f'\033[34m{file.read()}\033[m')
    print('\033[32mfim do arquivo\033[m'.center(50, '-'))
    print('\033[32m>\033[m Enter para continuar...', end='')
    input()
    file.seek(0)
    print('\033[32m>\033[m consoantes encontradas: ')
    print(list(filter(lambda consoante: consoante in consoantes, file.read())))
    file.seek(0)
    print(f'\033[32m>\033[m Quantidade de consoantes encontradas:'
          f' \033[32m{len(list(filter(lambda consoante: consoante in consoantes, file.read())))}\033[m consoantes.')
    file.seek(0)
    print('\033[32m>\033[m vogais encontradas: ')
    print(list(filter(lambda vogal: vogal in vogais, file.read())))
    file.seek(0)
    print(f'\033[32m>\033[m Quantidade de vogais encontradas:'
          f' \033[32m{len(list(filter(lambda vogal: vogal in vogais, file.read())))}\033[m vogais.')

