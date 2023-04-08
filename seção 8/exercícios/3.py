"""
Faca um funcao para verificar se um numero e positivo ou negativo.
Sendo que o valor de retorno sera 1 se positivo, -1 se negativo e 0 se for igual a 0
"""


def verifica_pos_neg(numero):
    if numero < 0:
        return -1
    elif numero > 0:
        return 1
    else:
        return 0


print(verifica_pos_neg(0))
