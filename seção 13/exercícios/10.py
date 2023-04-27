"""
Faça um programa que receba o nome de um arquivo de entrada e outro de saída.
O arquivo de entrada contém em cada linha o nome de uma cidade (ocupando 40 caracteres)
e o seu número de habitantes.
O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece o nome da cidade
mais populosa seguida pelo seu número de habitantes.
"""


def criar_arquivo_cidades():
    from os import listdir
    while True:
        arquivo_cidades = str(input('\033[32m>\033[m digite o nome do arquivo a ser criado \033[32m>\033[m ')).strip()
        if arquivo_cidades == '' or arquivo_cidades in listdir():
            print('\033[31merro : arquivo inválido, já existente ou nome vazio.\033[m')
            continue
        else:
            with open(arquivo_cidades, 'a+') as arq:
                pass
            return arquivo_cidades


def cadastrar_cidade(nome_arquivo):
    habitantes = 0
    while True:
        nome_cidade = str(input(
            '\033[32m>\033[m digite o nome da cidade [digite \033[32msair\033[m para finalizar] \033[32m>\033[m '
        )).strip().upper()
        if nome_cidade == 'SAIR':
            break
        if nome_cidade == '' or nome_cidade.isnumeric():
            print('\033[31merro : nome inválido.\033[m')
            continue
        else:
            while True:
                try:
                    habitantes = int(input('\033[32m>\033[m quantidade de habitantes \033[32m>\033[m '))
                except:
                    print('\033[31merro : nome inválido.\033[m')
                    continue
                else:
                    with open(nome_arquivo, 'a+') as arq:
                        arq.write(nome_cidade + '\n')
                        arq.write(str(habitantes) + '\n')
                        break
            continue


def procurar_maior_hab(nome_arquivo):
    from os import listdir
    maior_habitante = 0
    while True:
        arq_maior_cidade = str(input('\033[32m>\033[m digite o nome do arquivo de saída \033[32m>\033[m '))
        if arq_maior_cidade == '' or arq_maior_cidade in listdir():
            print('\033[31merro : arquivo inválido, já existente ou nome vazio.\033[m')
            continue
        else:
            with open(nome_arquivo, 'r') as arq:
                arquivo_string = arq.read().split('\n')
                for x, dado in enumerate(arquivo_string):
                    if dado.isnumeric() and int(dado) > maior_habitante:
                        maior_habitante = int(dado)
                        maior_cidade = arquivo_string[x - 1]
                        with open(arq_maior_cidade, 'w+') as arq_maior:
                            arq_maior.write(maior_cidade + '\n')
                            arq_maior.write(str(maior_habitante))
            return arq_maior_cidade


if __name__ == '__main__':
    from os import listdir
    arquivo_cidades = criar_arquivo_cidades()
    cadastrar_cidade(arquivo_cidades)
    arq_maior_cidade = procurar_maior_hab(arquivo_cidades)
    with open(arq_maior_cidade, 'r') as arq_maior:
        if arq_maior_cidade in listdir():
            print(f'\033[32m>\033[m arquivo \033[32m{arq_maior_cidade}\033[m criado com sucesso.')
        else:
            print('\033[31merro : finalizando o programa.\033[m')
        print(arq_maior.read())
