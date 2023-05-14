"""
Escreva um código que apresente a classe Quadrado, com atributos lado, área e perímetro e, os
métodos calcular_area(), calcular_perimetro() e imprimir().
Os métodos calcular_area e calcular_perimetro devem efetuar seus respectivos cálculos e colocar
os valores nos atributos área e perímetro.
O método imprimir deve mostrar na tela os valores de todos os atributos.
Salienta-se que a área de um quadrado é obtida pela fórmula lado x lado e o perímetro = 4 x lado.
"""


class Quadrado:

    __area = 0
    __perimetro = 0

    def __init__(self, lado):
        self.__lado = lado

    def calcular_area(self):
        self.__area = self.__lado * self.__lado

    def calcular_perimetro(self):
        self.__perimetro = 4 * self.__lado

    def imprimir(self):
        print(f'> lado : {self.__lado}')
        print(f'> área : {self.__area}')
        print(f'> perímetro : {self.__perimetro}')


quadrado = Quadrado(13)
quadrado.calcular_area()
quadrado.calcular_perimetro()
quadrado.imprimir()

