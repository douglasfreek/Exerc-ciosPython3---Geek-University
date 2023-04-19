"""
crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medidas dos tres lados
de um triângulo. Elabore funções para:
    - determinar se os lados formam um triângulo sabendo que:
        - o comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados
    - determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo.
    - denomina-se equilátero o triângulo que tem três lados iguais;
    - denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    - denomina-se escaleno o triângulo  que tem os três lados diferentes.
"""


def verifica_triangulo(a, b, c):
    """
    -> verifica se a medida dos três lados formam um triângulo
    """
    if a < (b + c) and b < (a + c) and c < (a + b):
        return True
    else:
        return False


def verifica_tipo(a, b, c):
    if verifica_triangulo(a, b, c):
        if a == b == c:
            return '\033[32m>\033[m triângulo equilátero'
        elif a == b and a != c or b == c and b != a or a == c and a != b:
            return '\033[32m>\033[m triângulo isósceles'
        else:
            return '\033[32m>\033[m triângulo escaleno'
    else:
        return '\033[31m erro\033[m : os valores enviados não podem formar um triângulo.'


def recebe_lado_a():
    while True:
        try:
            a = float(input('\033[32m>\033[m lado A: '))
        except:
            print('\033[31merro : valor inválido')
        else:
            return a


def recebe_lado_b():
    while True:
        try:
            b = float(input('\033[32m>\033[m lado B: '))
        except:
            print('\033[31merro : valor inválido')
        else:
            return b


def recebe_lado_c():
    while True:
        try:
            c = float(input('\033[32m>\033[m lado C: '))
        except:
            print('\033[31merro : valor inválido')
        else:
            return c


print('\033[32m>\033[m digite as medidas dos lados\033[32m <\033[m')
print('-' * 31)
print(verifica_tipo(recebe_lado_a(), recebe_lado_b(), recebe_lado_c()))
