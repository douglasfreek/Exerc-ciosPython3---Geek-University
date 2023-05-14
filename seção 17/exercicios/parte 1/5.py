"""
Escreva um código que apresente a classe Retangulo, com atributos comprimento, altura,
área e perímetro, e os métodos calcular_area, calcular_perimetro e imprimir.
Os métodos calcular_area e calcular_perimetro devem efetuar seus respectivos cálculos
e colocar os valores nos atributos area e perimetro.
O método imprimir deve mostrar na tela os valore de todos os atributos.
Salienta-se que a área de um retângulo é = comprimento * altura
e o perímetro = (2 * comprimento) + (2 * altura)
"""


class Retangulo:

    __area = 0
    __perimetro = 0

    def __init__(self, comprimento, altura):
        self.__comprimento = comprimento
        self.__altura = altura

    def calcular_area(self):
        self.__area = self.__comprimento * self.__altura

    def calcular_perimetro(self):
        self.__perimetro = (2 * self.__comprimento) + (2 * self.__altura)

    def imprimir(self):
        print(f'> comprimento : {self.__comprimento}')
        print(f'> altura : {self.__altura}')
        print(f'> área : {self.__area}')
        print(f'> perímetro : {self.__perimetro}')


retangulo = Retangulo(10, 5)
retangulo.calcular_perimetro()
retangulo.calcular_area()
retangulo.imprimir()
