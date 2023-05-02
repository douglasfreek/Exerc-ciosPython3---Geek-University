"""
Crie uma classe para representar uma pessoa, com os atributos privados de nome,
idade e altura. Crie os métodos públicos necessários para sets e gets e também
um método para imprimir os dados de uma pessoa.
"""


class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_altura(self, altura):
        self.__altura = altura

    def imprimir_pessoa(self):
        print(f'\033[32m>\033[m nome : {self.__nome}')
        print(f'\033[32m>\033[m idade : {self.__idade}')
        print(f'\033[32m>\033[m altura : {self.__altura}')


if __name__ == '__main__':
    pessoa1 = Pessoa('douglas', 37, 1.7)
    Pessoa.imprimir_pessoa(pessoa1)
    Pessoa.set_nome(pessoa1, 'Douglas dos Santos')  # alterando o nome da pessoa1
    Pessoa.imprimir_pessoa(pessoa1)
    Pessoa.set_idade(pessoa1, 38)  # alterando idade da pessoa1
    Pessoa.imprimir_pessoa(pessoa1)
    Pessoa.set_altura(pessoa1, 1.69)  # alterando altura da pessoa1
    Pessoa.imprimir_pessoa(pessoa1)
    print(Pessoa.get_nome(pessoa1))
    print(Pessoa.get_idade(pessoa1))
    print(Pessoa.get_altura(pessoa1))
