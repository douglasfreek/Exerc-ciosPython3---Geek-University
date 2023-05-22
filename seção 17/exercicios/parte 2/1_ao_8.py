"""
1 - Crie um novo pacote com o nome 'heranca'. Todas as três classes criadas abaixo deverão
ser salvas nesse pacote.

2 - Crie uma classe Equipamento com dois atributos privados.

3 - Crie uma classe Computador com dois atributos à sua escolha, também privados.
A classe Computador deverá herdar tudo da classe Equipamento.

4 - Crie os métodos de acesso e modificação para todos os atributos definidos em ambas
as classes.

5 - Crie uma classe TestaEquipamento, que deverá conter o método main(), crie nela um
objeto da classe Equipamento e instancie os dois atributos que você declarou na classe
Equipamento. Crie também um objeto da classe Computador, utilizando os dois atributos
declarados na própria classe e os dois herdados da classe Equipamento.

6 - O método main() deve exibir as informações dos dois objetos criados.

7 - Crie o método exibir() na classe Equipamento para mostrar os dados dessa classe.

8 - Reescreva o método exibir() na classe Computador, aproveitando o que já está escrito
na superclasse Equipamento.
"""


class Equipamento:

    def __init__(self, periferico_1, periferico_2):
        self.__periferico_1 = periferico_1
        self.__periferico_2 = periferico_2

    @classmethod
    def exibir(self):
        print(self.get_periferico_1)
        print(self.get_periferico_2)

    @property
    def get_periferico_1(self):
        return self.__periferico_1

    @property
    def get_periferico_2(self):
        return self.__periferico_2

    @get_periferico_1.setter
    def get_periferico_1(self, nome):
        self.__periferico_1 = nome

    @get_periferico_2.setter
    def get_periferico_2(self, nome):
        self.__periferico_2 = nome


class Computador(Equipamento):

    def __init__(self, periferico_1, periferico_2, processador, placa_video):
        super().__init__(periferico_1, periferico_2)
        self.__processador = processador
        self.__placa_video = placa_video

    @classmethod
    def exibir(self):
        print(self.get_periferico_1)
        print(self.get_periferico_2)
        print(self.get_processador)
        print(self.get_placa_video)

    @property
    def get_processador(self):
        return self.__processador

    @property
    def get_placa_video(self):
        return self.__placa_video

    @get_processador.setter
    def get_processador(self, nome):
        self.__processador = nome

    @get_placa_video.setter
    def get_placa_video(self, nome):
        self.__placa_video = nome


class TestaEquipamento:

    perifericos = Equipamento
    pc = Computador

    def __init__(self, perif_1, perif_2, processador, placa_video):
        self.perifericos.get_periferico_1 = perif_1
        self.perifericos.get_periferico_2 = perif_2
        self.pc.get_processador = processador
        self.pc.get_placa_video = placa_video

    @classmethod
    def exibir(self):
        print(self.pc.get_periferico_1)
        print(self.pc.get_periferico_2)
        print(self.pc.get_processador)
        print(self.pc.get_placa_video)


perif = Equipamento
perif.get_periferico_1 = 'teclado'
perif.get_periferico_2 = 'mouse'

pc = Computador
pc.get_periferico_1 = 'teclado'
pc.get_periferico_2 = 'mouse'
pc.get_processador = 'ryzen 5'
pc.get_placa_video = 'rx 5600 xt'
pc.exibir()

teste = TestaEquipamento
teste.exibir()
print(teste.pc.get_placa_video)
print(teste.pc.get_processador)
print(teste.perifericos.get_periferico_1)
print(teste.perifericos.get_periferico_2)
