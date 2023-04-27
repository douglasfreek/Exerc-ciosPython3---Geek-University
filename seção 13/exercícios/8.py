"""
Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo,
mas com todas as letras minúsculas convertidas para maiúsculas.
Os nomes dos arquivos serão fornecidos via teclado pelo usuário.
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
            else:
                return op


def nome_copia():
    while True:
        nome_copia = str(input('\033[32m>\033[m digite o nome do arquivo cópia \033[32m>\033[m ')).strip()
        if nome_copia == '' or nome_copia in os.listdir():
            print('\033[31merro : nome inválido (arquivo já existente ou nome vazio)\033[m')
        else:
            return nome_copia


arquivo_orig = menu()
copia_nome = nome_copia()
with open(arquivo_orig, 'r') as arquivo:
    arquivo_copia = arquivo.read().upper()
with open(copia_nome, 'w+') as copia:
    copia.write(arquivo_copia)
    print(f'\033[32m>\033[m arquivo \033[32m{copia_nome}\033[m criado com sucesso.')
    print('\033[32m>\033[m Enter para abrir o arquivo criado...', end='')
    input()
    copia.seek(0)
    print(f'\033[34m{copia.read()}\033[m')
