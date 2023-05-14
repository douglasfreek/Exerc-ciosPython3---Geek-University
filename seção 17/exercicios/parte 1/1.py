"""
Escreva um código que apresente a classe Pessoa, com atributos nome, endereço e telefone, e o
método imprimir, que deve mostrar na tela os valores de todos os atributos.
"""


class Pessoa:

    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    def imprimir(self):
        print(f'{self.__nome}')
        print(f'{self.__telefone}')
        print(f'{self.__endereco}')


pessoa = Pessoa('Tobias', 'Planeta Terra', '999-999-999')
pessoa.imprimir()