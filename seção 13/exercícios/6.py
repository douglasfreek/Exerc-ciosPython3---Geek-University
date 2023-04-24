"""
Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto aparece
dentro do arquivo.
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


caracteres = 'qwertyuiopasdfghjklzxcvbnméúíóáçãõà'
arq = menu()
with open(arq, 'r') as arquivo:
    arquivo_read = arquivo.read()
    print(f'\033[32m>\033[m arquivo selecionado : \033[32m{arq}\033[m')
    print(f'\033[34m{arquivo_read}\033[m')
    mapa_caract = {letra: arquivo_read.count(letra) for letra in arquivo_read.lower() if letra in caracteres}
print('\033[32m>\033[m Caracteres mapeados e suas quantidades :')
for letra, quant in mapa_caract.items():
    print(f'> \033[32m{letra}\033[m > \033[32m{quant}\033[m vez(es)')
