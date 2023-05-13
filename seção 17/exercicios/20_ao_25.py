"""
20 - Escreva um código que apresente a classe Televisor, com atributos ligado, canal e volume
e o método imprimir.
O método imprimir deve mostrar na tela os valores de todos os atributos.
O atributo ligado será booleano e deverá indicar o estado atual do televisor, ligado ou desligado.
O atributo canal deverá indicar o canal atual em que o televisor está sintonizado.
O atributo volume deverá indicar o volume atual do televisor.

21 - Adicione um método construtor que permita a definição de todos os atributos no momento da
instanciação do objeto.

22 - Adicione os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligado.

23 - Adicione os atributos numero_canais e volume_maximo, onde numero_canais indica o número
máximo de canais que o televisor pode sintonizar e volume_maximo indica qual o maior nível
de volume possível. O método imprimir deve ser modificado de forma a mostrar na tela
os valores de todos os atributos.

24 - Adicione os métodos canal_acima e canal_abaixo, sendo que o método canal_acima deve
sintonizar sempre o próximo canal em relação ao atual, onde, ao chegar ao maior canal
possível deverá voltar ao canal 1. O método canal_abaixo deve sintonizar sempre o canal
anterior em relação ao canal atual, onde, ao chegar ao canal 1, deverá voltar ao maior
canal possível, simulando desta forma o funcionamento de um televisor.

25 - Adicione os métodos volume_acima e volume_abaixo, sendo que o método volume_acima
deve modificar o volume para o próximo nível de volume possível, onde ao chegar ao volume
máximo não poderá possibilitar que o volume seja alterado.
O método volume_abaixo deve modificar o volume para o nível imediatamente inferior
de volume em relação ao volume atual, não podendo ser menor que 0, simulando desta forma
o funcionamento de um televisor.
"""


class Televisor:

    def __init__(self, canal, volume, max_canal, max_volume, ligado=False):
        self.__canal = canal
        self.__volume = volume
        self.__ligado = ligado
        self.__max_canal = max_canal
        self.__max_volume = max_volume

    def imprimir(self):
        print('\n\033[32mTv ligada\033[m' if self.__ligado else '\n\033[31mTv desligada\033[m')
        print(f'Canal      : {self.__canal}')
        print('Volume     :', end=' '), print('\033[31mMute\033[m' if self.__volume == 0 else self.__volume)
        print(f'Max canal  : {self.__max_canal}')
        print(f'Max volume : {self.__max_volume}')

    def liga_desliga(self):
        if not self.__ligado:
            self.__ligado = True
        else:
            self.__ligado = False

    def canal_acima(self):
        if self.__canal == self.__max_canal:
            self.__canal = 1
        else:
            self.__canal += 1

    def canal_abaixo(self):
        if self.__canal == 1:
            self.__canal = self.__max_canal
        else:
            self.__canal -= 1

    def volume_acima(self):
        if self.__volume < self.__max_volume:
            self.__volume += 1

    def volume_abaixo(self):
        if self.__volume > 0:
            self.__volume -= 1


tv = Televisor(1, 1, 10, 10)
tv.imprimir()
tv.liga_desliga()
tv.canal_acima()
tv.canal_acima()
tv.canal_acima()
tv.canal_abaixo()
tv.volume_acima()
tv.volume_acima()
tv.volume_abaixo()
tv.imprimir()
