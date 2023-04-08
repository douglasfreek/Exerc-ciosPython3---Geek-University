"""
Faca uma funcao que receba a data atual (dia, mes e ano em inteiro) e exiba-a na tela no formato textual por extenso.
Ex: data: 01/01/2000. imprimir: 1 de janeiro de 2000.
"""


def funcao_mes(mes):
    if mes == 1:
        return 'janeiro'
    elif mes == 2:
        return 'fevereiro'
    elif mes == 3:
        return 'marco'
    elif mes == 4:
        return 'abril'
    elif mes == 5:
        return 'maio'
    elif mes == 6:
        return 'junho'
    elif mes == 7:
        return 'julho'
    elif mes == 8:
        return 'agosto'
    elif mes == 9:
        return 'setembro'
    elif mes == 10:
        return 'outubro'
    elif mes == 11:
        return 'novembro'
    elif mes == 11:
        return 'dezembro'


def data_atual(dia, mes, ano):
    return f'{dia} de {funcao_mes(mes)} de {ano}'


def receber_dia():
    while True:
        try:
            dia = int(input('\033[32mDia\033[m : '))
        except:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            if dia < 1 or dia > 31:
                print('\033[31merro : valor inválido\033[m')
                continue
            else:
                return dia


def receber_mes():
    while True:
        try:
            mes = int(input('\033[32mMes\033[m : '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if mes < 1 or mes > 12:
                print('\033[31merro : valor inválido\033[m')
                continue
            else:
                return mes


def receber_ano():
    while True:
        try:
            ano = int(input('\033[32mAno\033[m : '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if ano < 1:
                print('\033[31merro : valor inválido\033[m')
                continue
            elif len(str(ano)) < 4 or len(str(ano)) > 4:
                print('\033[31merro : valor inválido\033[m')
                continue
            else:
                return ano


data = data_atual(receber_dia(), receber_mes(), receber_ano())
print(f'\n\033[32m>\033[m {data}')
