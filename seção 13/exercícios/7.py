"""
Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo contendo o texto
do arquivo de entrada, mas com as vogais substituídas por '*'
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


file = menu()
with open(file, 'r') as arquivo:
    vogais = 'aeiouáéíóúãõà'
    arquivo_read = arquivo.read()
    with open('arquivo_cript', 'w+') as arquivo_cript:
        for letra in arquivo_read.lower():
            if letra in vogais:
                arquivo_cript.write('*')
            else:
                arquivo_cript.write(letra)
        arquivo_cript.seek(0)
        print(f'\033[32m>\033[m Arquivo original\n\n\033[34m{arquivo_read}\033[m')
        print(f'\n\033[32m>\033[m Arquivo criptografado\n\n\033[34m{arquivo_cript.read()}\033[m')
