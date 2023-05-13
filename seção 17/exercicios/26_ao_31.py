"""
26 - Escreva um código que apresente a classe Microondas, com atributo ligado e o método imprimir.
O método imprimir deve mostrar na tela os valores de todos os atributos.
O atributo ligado será booleano, e deverá indicar o estado atual do microondas, ligado ou não.

27 - Adicione um método construtor que permita a definição de todos os atributos no momento
da instanciação do objeto.

28 - Adicione os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligado.

29 - Adicione o atributo porta_fechada que deverá ser booleano e deverá indicar se a porta
do microondas está ou não fechada. O método imprimir deve ser modificado de forma
a mostrar na tela os valores de todos os atributos.

30 - Adicione os métodos fechar_porta e abrir_porta que deverá mudar o conteúdo do atributo
porta_fechada conforme o caso.

31 - Modifique o método ligar para que só ligue o equipamento caso a porta esteja fechada,
simulando assaim o funcionamento de um microondas.
"""


class Microondas:

    def __init__(self, ligado=False, porta_fechada=True):
        self.__ligado = ligado
        self.__porta_fechada = porta_fechada

    def imprimir(self):
        print('\033[32mMicroondas ligado\033[m' if self.__ligado else '\033[31mMicroondas desligado\033[m')
        print('\033[32mPorta fechada\033[m' if self.__porta_fechada else '\033[31mPorta aberta\033[m')

    def liga_desliga(self):
        if not self.__ligado and self.__porta_fechada:
            self.__ligado = True
        else:
            self.__ligado = False

    def abrir_porta(self):
        if self.__porta_fechada:
            self.__porta_fechada = False
            self.__ligado = False

    def fechar_porta(self):
        if not self.__porta_fechada:
            self.__porta_fechada = True


micro = Microondas()
micro.imprimir()
micro.liga_desliga()
micro.imprimir()
micro.abrir_porta()
micro.imprimir()
micro.liga_desliga()
micro.imprimir()
micro.fechar_porta()
micro.imprimir()
micro.liga_desliga()
micro.imprimir()
micro.abrir_porta()
micro.imprimir()

