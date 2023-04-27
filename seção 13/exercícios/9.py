"""
Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o conteúdo dos dois
primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo)
"""
import os


def menu():
    """
    -> cria um menu com todos os arquivos que estão na pasta atual, cada um com um número para ser selecionado.
    :return: retorna o nome do arquivo de número escolhido
    """
    print('\033[32m>\033[m selecione um arquivo para ser copiado na pasta abaixo : ')
    print(f'\033[32m{os.getcwd()}\033[m')
    print('\033[32m>\033[m')
    for file in os.listdir():
        print(f'\t\033[32m>\033[m {file}')
    while True:
        try:
            op = str(input('\033[32m>\033[m digite o nome do arquivo \033[32m>\033[m ')).strip()
        except:
            print('\033[31merro : arquivo inválido\033[m')
        else:
            if op == '' or op not in os.listdir():
                print('\033[31merro : arquivo inválido\033[m')
                continue
            else:
                return op


def segundo_arq():
    while True:
        try:
            seg = str(input('\033[32m>\033[m digite o nome do segundo arquivo \033[32m>\033[m ')).strip()
        except:
            print('\033[31merro : arquivo inválido\033[m')
        else:
            if seg == '' or seg not in os.listdir():
                print('\033[31merro : arquivo inválido\033[m')
                continue
            else:
                return seg


def terceiro_arq():
    while True:
        try:
            ter = str(input('\033[32m>\033[m digite o nome do arquivo resultante \033[32m>\033[m ')).strip()
        except:
            print('\033[31merro : arquivo inválido\033[m')
        else:
            if ter == '' or ter in os.listdir():
                print('\033[31merro : nome inválido (arquivo já existente ou nome vazio)\033[m')
            else:
                return ter


with open(menu(), 'r') as arquivo_1:
    with open(segundo_arq(), 'r') as arquivo_2:
        with open(terceiro_arq(), 'a+') as arquivo_3:
            arquivo_3.write(arquivo_1.read() + arquivo_2.read())
            arquivo_3.seek(0)
            print(arquivo_3.read())
