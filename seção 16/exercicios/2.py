"""
Crie uma classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar as seguintes operações:
    - armazena_pessoa(nome, idade, altura)
    - remove_pessoa(nome)
    - busca_pessoa(nome)  -->  informa em qual posição da agenda está a pessoa
    - imprime_agenda()  -->  imprime os dados de todas as pessoas da agenda
    - imprime_pessoa()  -->  imprime os dados da pessoa que está na posição 'i' da agenda.
"""



class Agenda:
    __agenda = []

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def cadastrar_pessoa(self):
        """Armazena os dados na agenda."""
        if len(self.__agenda) < 4:
            self.__agenda.append([self.__nome, self.__idade, self.__altura])
            return f'> \033[32m{self.__nome}\033[m cadastrado com sucesso.'
        else:
            return '\033[31m>\033[37m erro : memória da agenda está cheia\033[m'

    @classmethod
    def imprime_agenda(cls):
        """Imprime na tela todas as pessoas cadastradas na agenda."""
        return cls.__agenda

    @classmethod
    def busca_pessoa(cls, nome):
        """Busca pessoa pelo nome e retorna seu índice"""
        for i, pessoa in enumerate(cls.__agenda):
            if nome == (pessoa[0]):
                return i



    @classmethod
    def imprime_pessoa(cls, indice):
        """Imprime uma pessoa da agenda de acordo com o seu índice"""
        if indice < 0 or indice >= len(cls.__agenda):
            return '\033[31m>\033[37m erro - índice inexistente\033[m'
        else:
            for i, pessoa in enumerate(cls.__agenda):
                if indice == i:
                    return pessoa

    @classmethod
    def remove_pessoa(cls, nome):
        """Remove pessoa pelo nome completo"""
        for i, pessoa in enumerate(cls.__agenda):
            if nome == pessoa[0]:
                cls.__agenda.pop(i)
                return f'\033[32m>\033[m Contato \033[32m{pessoa[0]}\033[m removido(a).'
            else:
                return f'\033[32m>\033[m {nome} não encontrado. Tente o nome completo.'


def menu():
    print('''
    \033[32ma g e n d a\033[m
    
    \033[32m[ 1 ]\033[m - cadastrar pessoa
    \033[32m[ 2 ]\033[m - imprimir agenda
    \033[32m[ 3 ]\033[m - buscar pessoa
    \033[32m[ 4 ]\033[m - imprimir pessoa
    \033[32m[ 5 ]\033[m - remover pessoa
    \033[32m[ 6 ]\033[m - sair
    ''')
    while True:
        try:
            operacao = int(input('opção \033[32m>\033[m '))
        except:
            print('\033[31m>\033[37m erro : opção inválida\033[m')
        else:
            if operacao < 1 or operacao > 6:
                print('\033[31m>\033[37m erro : opção inválida\033[m')
                continue
            else:
                return operacao


while True:
    op = menu()
    print()
    if op == 6:
        break
    elif op == 1:
        while True:
            nome_ = str(input('\033[32m>\033[m nome   : ')).strip().lower()
            if nome_ == '':
                print('\033[31m>\033[37m erro : nome não pode estar vazio\033[m')
                continue
            else:
                break
        while True:
            try:
                idade_ = int(input('\033[32m>\033[m idade  : '))
            except:
                print('\033[31m>\033[37m erro : valor inválido\033[m')
                continue
            else:
                break
        while True:
            try:
                altura_ = float(input('\033[32m>\033[m altura : '))
            except:
                print('\033[31m>\033[37m erro : valor inválido\033[m')
                continue
            else:
                break
        print(Agenda.cadastrar_pessoa(Agenda(nome_, idade_, altura_)))
    if op == 2:
        print('-' * 84)
        for pessoa in Agenda.imprime_agenda():
            print(f'\033[32m> nome :\033[m {pessoa[0].title():<30}   |   '
                  f'\033[32m> idade :\033[m {pessoa[1]:<2}   |   '
                  f'\033[32m> altura :\033[m {pessoa[2]:.2f}   |')
        print('-' * 84)
    if op == 3:
        nome = str(input('\033[32m>\033[m buscar nome : ')).strip().lower()
        busca_pessoa = Agenda.busca_pessoa(nome)
        if busca_pessoa == None:
            print(f'\033[32m>\033[m {nome} não encontrado. Tente o nome completo.')
        else:
            print(f'\033[32m>\033[m índice de \033[32m{nome.title()}\033[m = \033[32m{busca_pessoa}\033[m')
    if op == 4:
        indice = int(input('\033[32m>\033[m imprimir índice : '))
        print()
        if indice < 0 or indice >= len(Agenda.imprime_agenda()):
            print(Agenda.imprime_pessoa(indice))
        else:
            print('-' * 84)
            print(f'\033[32m> nome :\033[m {Agenda.imprime_pessoa(indice)[0].title():<30}   |   '
                  f'\033[32m> idade :\033[m {Agenda.imprime_pessoa(indice)[1]:<2}   |   '
                  f'\033[32m> altura :\033[m {Agenda.imprime_pessoa(indice)[2]:.2f}   |')
            print('-' * 84)
    if op == 5:
        nome = str(input('\033[32m>\033[m nome para remover : ')).strip().lower()
        print(Agenda.remove_pessoa(nome))
