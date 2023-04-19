"""
Faça uma função que receba dois números inteiros positivos por parâmetro e retorne a soma dos
N números inteiros existentes entre eles.
"""

def intervalo(inicio, fim):
    """
    retorna a soma dos números inteiros entre o intervalo fornecido.
    obs: os valores final e inicial NÃO entram na somatória.
    :param x: início do intervalo
    :param y: fim do intervalo
    :return: soma dos números inteiros entre o intervalo
    """
    return sum(0 + n for n in range(inicio + 1, fim))


print(intervalo(1, 3))
