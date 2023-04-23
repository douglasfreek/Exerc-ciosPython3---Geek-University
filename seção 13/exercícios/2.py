"""
Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo possui
"""
import os
from time import sleep


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
            op = int(input('\033[32m>\033[m opcao: '))
        except:
            print('valor inválido')
        else:
            if op >= len(os.listdir()) or op < 0:
                print('erro : valor inválido')
                continue
            else:
                return os.listdir()[op]


arquivo = menu()
sleep(0.5)
print(f'\n\033[32m>\033[m arquivo selecionado : \033[32m{arquivo}\033[m')
sleep(0.5)
with open(arquivo, 'r') as file:
    print(f'\033[32m>\033[m O arquivo \033[32m{arquivo}\033[m tem \033[32m{len(file.readlines())}\033[m linha(s).')
sleep(0.5)
print('\033[32m>\033[m pressione Enter para finalizar.')
input()
