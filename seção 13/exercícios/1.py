"""
Escreva um programa que:
    - Crie/abra um arquivo texto de nome 'arq.txt'
    - Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere 0
    - Feche o arquivo

Agora abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados.
"""
with open('arq.txt', 'w+') as arq:
    while True:
        carac = str(input('\033[32m>\033[m digite um caractere para gravar no arquivo [0 - sair] : '))
        if carac == '0':
            print('\033[32m>\033[m finalizando...')
            break
        else:
            arq.write(carac)
    arq.seek(0)
    print(f'\033[32m>\033[m Os caracteres digitados foram: {[car for car in arq.read()]}')
print(f'\033[32m>\033[m o arquivo foi fechado? \033[32m{arq.closed}\033[m')
