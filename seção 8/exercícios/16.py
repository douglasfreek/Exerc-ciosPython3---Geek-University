"""
Faça uma função que desenhe uma linha na tela usando vários símbolos de =.
A função recebe por parâmetro quantos sinais de igual serão mostrados.
"""


def desenha_linha():
    while True:
        try:
            tam_linha = int(input('\033[32m>\033[m Tamanho da linha: '))
        except:
            print('\033[31merro : valor inválido')
        else:
            return '=' * tam_linha


print(desenha_linha())
