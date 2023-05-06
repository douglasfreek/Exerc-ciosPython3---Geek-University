"""
Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio.
A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio,
excluindo o térreo, capacidade do elevador, e quantas pessoas estão presentes nele.

A classe deve disponibilizar os seguintes métodos:
    - Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio
                  (o elevador sempre começa no térreo e vazio);
    - Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço)
    - Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele)
    - Sobe: para subir um andar (não deve subir se já estiver no último andar)
    - Desce: para descer um andar (não deve descer se já estiver no térreo)

Encapsular todos os atributos da classe (criar os métodos setters e getters)
"""


class Elevador:

    def __init__(self, total_andares, capacidade, andar_atual=0, ocupantes=0):
        self.__andar_atual = andar_atual
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__ocupantes = ocupantes

    @property
    def get_andar_atual(self):
        return self.__andar_atual

    @property
    def get_total_andares(self):
        return self.__total_andares

    @property
    def get_capacidade(self):
        return self.__capacidade

    @property
    def get_ocupantes(self):
        return self.__ocupantes

    def entra(self):
        if self.__ocupantes < self.__capacidade:
            self.__ocupantes += 1
        else:
            print('\n\033[31m>\033[37m erro : elevador está cheio\033[m')

    def sai(self):
        if self.__ocupantes > 0:
            self.__ocupantes -= 1
        else:
            print('\n\033[31m>\033[37m erro : elevador está vazio\033[m')

    def sobe(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
        else:
            print('\n\033[31m>\033[37m erro : elevador já está no último andar\033[m')

    def desce(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
        else:
            print('\n\033[31m>\033[37m erro : elevador já está no térreo\033[m')



while True:
    try:
        capacidade = int(input('\033[32m>\033[m digite a capacidade total do elevador : '))
    except:
        print('\033[31m>\033[37m erro : valor inválido\033[m')
    else:
        if capacidade <= 0:
            print('\033[31m>\033[37m erro : valor inválido\033[m')
        else:
            break
while True:
    try:
        andares = int(input('\033[32m>\033[m digite a quantidade total de andares, excluindo o térreo  : '))
    except:
        print('\033[31m>\033[37m erro : valor inválido\033[m')
    else:
        if andares <= 0:
            print('\033[31m>\033[37m erro : valor inválido\033[m')
        else:
            break
elevador = Elevador(andares, capacidade)
while True:
    print(f'''
    \033[32me l e v a d o r\033[m
    
    \033[32m>\033[m andar atual : \033[34m{"térro" if elevador.get_andar_atual == 0 else elevador.get_andar_atual}\033[m
    \033[32m>\033[m ocupantes   : \033[34m{elevador.get_ocupantes}\033[m
    
    [ \033[32m1\033[m ] adicionar uma pessoa
    [ \033[32m2\033[m ] retirar uma pessoa
    [ \033[32m3\033[m ] subir um andar
    [ \033[32m4\033[m ] descer um andar
    [ \033[32m0\033[m ] finalizar programa
    ''')

    while True:
        try:
            operacao = int(input('\033[32m>\033[m opção : '))
        except:
            print('\033[31m>\033[37m erro : valor inválido\033[m')
        else:
            if operacao < 0 or operacao > 4:
                print('\033[31m>\033[37m erro : valor inválido\033[m')
                continue
            else:
                break
    if operacao == 0:
        print('saindo...')
        break
    if operacao == 1:
        elevador.entra()
    if operacao == 2:
        elevador.sai()
    if operacao == 3:
        elevador.sobe()
    if operacao == 4:
        elevador.desce()
