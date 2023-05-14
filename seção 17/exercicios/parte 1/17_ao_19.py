"""
17 - Escreva um código que apresente a classe Eletrodomestico, com atributo ligado e o
método imprimir.
O método imprimir deve mostrar na tela os valores de todos os atributos.
O atributo ligado será booleano e deverá indicar o estado atual do eletrodoméstico, ligado ou desligado.

18 - Adicione um método construtor que permita a definição de todos os atirebutos no momento
da instanciação do objeto.

19 - Adicione os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligado.
"""


class Eletrodomestico:

    def __init__(self, ligado=False):
        self.ligado = ligado

    def imprimir(self):
        print('Desligado' if not self.ligado else 'Ligado')

    def ligar_desligar(self):
        if not self.ligado:
            self.ligado = True
        else:
            self.ligado = False


tv = Eletrodomestico()
tv.imprimir()
tv.ligar_desligar()
tv.imprimir()
tv.ligar_desligar()
tv.imprimir()
