"""
Escreva um código que apresente a classe Circulo, com atributos raio, área e perímetro, e os
métodos calcular_area, calcular_perimetro e imprimir. Os métodos calcular_area e calcular_perimetro
devem efetuar seus respectivos cálculos e colocar os valores nos atributos area e perimetro.
O método imprimir deve mostrar na tela os valores de todos os atributos.
Salienta-se que a área do círculo = pi * raio ** 2
e o perímetro = 2 * pi * raio
pi = 3.141516
"""


class Circulo:

    __area = 0
    __perimetro = 0
    __pi = 3.141516

    def __init__(self, raio):
        self.__raio = raio

    def calcular_area(self):
        self.__area = self.__pi * self.__raio ** 2

    def calcular_perimetro(self):
        self.__perimetro = 2 * self.__pi * self.__raio

    def imprimir(self):
        print(f'> pi : {self.__pi}')
        print(f'> raio : {self.__raio}')
        print(f'> área : {self.__area:.2f}')
        print(f'> perímetro : {self.__perimetro:.2f}')


circulo = Circulo(5)
circulo.calcular_area()
circulo.calcular_perimetro()
circulo.imprimir()
