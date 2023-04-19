"""
Faça uma função que receba a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:

CONSUMO     KM/L      MENSAGEM
menor que    8        venda o carro
entre      8 e 14     economico
maior que   12        super economico
"""


def distancia():
    while True:
        try:
            distancia = float(input('\033[32m>\033[m Distância da viagem : '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if distancia <= 0:
                print('\033[31merro : valor inválido\033[m')
            else:
                return distancia


def consumo():
    while True:
        try:
            consumo = float(input('\033[32m>\033[m Consumo, em litros, do combústivel utilizado na viagem : '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if consumo <= 0:
                print('\033[31merro : valor inválido\033[m')
            else:
                return consumo


def media(distancia, consumo):
    return distancia / consumo


media = media(distancia(), consumo())
print(f'\033[32m>\033[m Autonomia : {media:.2f} Km/l')
if media < 8:
    print('\033[31m> venda o carro ! <\033[m')
elif 8 <= media < 14:
    print('\033[33m> econômico ! <\033[m')
else:
    print('\033[34m> super econômico ! <\033[m ')
