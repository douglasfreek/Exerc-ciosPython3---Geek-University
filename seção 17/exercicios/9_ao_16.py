"""
9 - Escreva um código que apresente a classe Moto, com atributos marca, modelo, cor e marcha,
e o método imprimir.
O método imprimir deve mostrar na tela os valores de todos os atributos.
O atributo marcha indica em que marcha a moto se encontra no momento, sendo representado
de forma inteira, onde 0 é neutro, 1 primera, etc...

10 - Adicione um método construtor que permita a definição de todos os atributos no momento da
instanciação do objeto.

11 - Adicione os métodos marcha_acima e marcha_abaixo que deverão efetuar a troca de marchas,
onde o método marcha_acima deverá subir uma marcha, ou seja, se a moto estiver em primeira
marcha, deverá ser trocada para a segunda marcha e assim por diante.
O método marcha abaixo deverá realizar o oposto, ou seja, descer a marcha.
O método imprimir deve ser modificado de forma a mostrar na tela o valor de todos os atributos.

12 - Adicione os atributos menor_marcha e maior_marcha, onde o atributo menor_marcha indica qual
será a menor marcha possível para a moto e o atributo maior_marcha indica qual será a maior marcha possível.
Desta forma os métodos marcha_acima e marcha_abaixo devem ser reescritos de forma a não permitirem a troca
de marchas para valores abaixo de menor_marcha e acima de maior_marcha.
O método imprimir deve ser modificado de forma a mostrar na tela o valor de todos os atributos.

13 - Adicione um método construtor que permita a definição de todos os atributos no momento da instanciação
do objeto.

14 - Adicione o atributo ligada que terá a função de indicar se a moto está ligada ou desligada.
Este atributo deverá ser do tipo booleano. O método imprimir deve ser modificado de forma a mostrar
na tela o valor de todos os atributos.

15 - Adicione um método construtor que permita a definição de todos os atributos no momento da
instanciação do objeto.

16 - Adicione os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligada conforme o caso.

"""


class Moto:

    def __init__(self, marca, modelo, cor, marcha, menor_marcha, maior_marcha, ligada=False):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.menor_marcha = menor_marcha
        self.maior_marcha = maior_marcha
        self.ligada = ligada

    def __str__(self):
        return f'{self.marca} {self.modelo}'

    def imprimir(self):
        print(f'Marca        : {self.marca}')
        print(f'Modelo       : {self.modelo}')
        print(f'Cor          : {self.cor}')
        print(f'Marcha       : {self.marcha}')
        print(f'Menor marcha : {self.menor_marcha}')
        print(f'Maior marcha : {self.maior_marcha}')
        print(f'Ligada       : {"sim" if self.ligada else "não"}')

    def marcha_acima(self):
        if self.marcha < self.maior_marcha:
            self.marcha += 1

    def marcha_abaixo(self):
        if self.marcha > self.menor_marcha:
            self.marcha -= 1

    def liga_desliga(self):
        if not self.ligada:
            self.ligada = True
        else:
            self.ligada = False


moto = Moto('Honda', 'Titan', 'Preta', 0, 0, 5)
moto.imprimir()
moto.liga_desliga()
moto.marcha_acima()
moto.marcha_acima()
moto.marcha_abaixo()
moto.imprimir()
