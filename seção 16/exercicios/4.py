"""
Crie uma classe Televisao e uma classe ControleRemoto que pode controlar o volume e trocar canais da tv.
    - O controle de volume permite aumentar ou diminuir o volume em uma unidade de cada vez;
    - O controle de canal permite aumentar e diminuir o número do canal em uma unidade, porém,
      também possibilita trocar para um canal indicado;
    - Criar métodos para consultar o valor do volume e do canal atual.
"""


class Televisao:

    def __init__(self, max_canais, max_volume):
        """
        construtor do objeto Televisao
        - max_canais = quantidade máxima de canais que a tv suporta
        - max_volume = volume máximo que a tv alcança
        """
        self.__canal_atual = 1
        self.__volume_atual = 1
        self.__max_volume = max_volume
        self.__max_canal = max_canais
        self.__ligada = False

    @property
    def estado(self):
        """retorna o estado atual da tv, ligada ou desligada"""
        return self.__ligada

    @property
    def canal(self):
        """retorna o canal atual que a tv está sintonizada"""
        return self.__canal_atual

    @property
    def volume(self):
        """retorna o volume de som atual da tv"""
        return self.__volume_atual

    @property
    def max_volume(self):
        """retorna o volume máximo que a tv alcança (um dos parâmetros iniciais para construção do objeto tv)"""
        return self.__max_volume

    @property
    def max_canal(self):
        """retorna o canal máximo que a tv alcança (um dos parâmetros iniciais para construção do objeto tv)"""
        return self.__max_canal

    def set_volume(self, volume):
        """altera o volume atual da tv"""
        self.__volume_atual = volume

    def set_canal(self, canal):
        """altera o canal atual da tv"""
        self.__canal_atual = canal

    def set_estado(self):
        """altera o estado atual da tv (liga ou desliga)"""
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ControleRemoto:

    def __init__(self, televisao):
        """construtor do obj ControleRemoto, recebe como parâmetro a tv que ele vai controlar"""
        self.televisao = televisao

    def liga_desliga(self):
        """altera o estado da tv (liga e desliga)"""
        self.televisao.set_estado()

    def mais_volume(self):
        """aumenta o volume da tv em 1 unidade, até o máximo que a tv suporta"""
        if self.televisao.estado:
            if self.televisao.volume < self.televisao.max_volume:
                self.televisao.set_volume(self.televisao.volume + 1)

    def menos_volume(self):
        """diminui o volumet da tv em 1 unidade, até o mínimo 0"""
        if self.televisao.estado:
            if self.televisao.volume > 0:
                self.televisao.set_volume(self.televisao.volume - 1)

    def mais_canal(self):
        """altera o canal em 1 unidade para mais"""
        if self.televisao.estado:
            if self.televisao.canal < self.televisao.max_canal:
                self.televisao.set_canal(self.televisao.canal + 1)

    def menos_canal(self):
        """altera o canal em 1 unidade para menos"""
        if self.televisao.estado:
            if self.televisao.canal > 0:
                self.televisao.set_canal(self.televisao.canal - 1)

    def set_canal(self, canal):
        """altera para um número de canal específico, de 0 até o máximo que a tv suporte"""
        if self.televisao.estado:
            if 0 <= canal <= self.televisao.max_canal:
                self.televisao.set_canal(canal)


tv = Televisao(99, 10)
controle = ControleRemoto(tv)
while True:
    print(f'''
     ________________________________
    |                                |
    |              T  V              |
    |                                |
     --------------------------------
     Estado: \033[32m{'TV Ligada' if tv.estado == True else 'TV Desligada'}\033[m
     Canal: \033[32m{tv.canal if tv.estado == True else 'TV Desligada'}\033[m
     Volume: \033[32m{tv.volume if tv.estado == True else 'TV Desligada'}\033[m
    ''', end='')
    print('''
    controle remoto:
    
         [ 0 ] liga / desliga
    
    [ 1 ] + canal     [ 3 ] + volume
    [ 2 ] - canal     [ 4 ] - volume
    
         [ 5 ] escolher canal
         [ 6 ] sair do programa
    ''')
    while True:
        try:
            operacao = int(input('opção : '))
        except:
            print('\033[31m>\033[37m erro : opção inválida\033[m')
            continue
        else:
            if operacao < 0 or operacao > 6:
                print('\033[31m>\033[37m erro : opção inválida\033[m')
            else:
                break
    if operacao == 6:
        break
    if operacao == 0:
        controle.liga_desliga()
    if operacao == 1:
        controle.mais_canal()
    if operacao == 2:
        controle.menos_canal()
    if operacao == 3:
        controle.mais_volume()
    if operacao == 4:
        controle.menos_volume()
    if operacao == 5:
        while True:
            try:
                canal = int(input('canal : '))
            except:
                print('\033[31m>\033[37m erro : opção inválida\033[m')
            else:
                break
        controle.set_canal(canal)
