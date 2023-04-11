"""
Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro.
O volume de um cilindro circular é calculado por meio da seguinte fórmula:
V = pi * raio ** 2 * altura
pi = 3.141592
"""


def volume_cilindro(altura, raio):
    """
    -> Recebe altura e raio de um cilindro para retornar seu volume.
    :param altura: altura do cilindro
    :param raio: raio do cilindro
    :return: volume do cilindro
    """
    pi = 3.141592
    return pi * raio ** 2 * altura


volume = volume_cilindro(altura=float(input('\033[32m>\033[m Altura do cilindro : ')),
                raio=float(input('\033[32m>\033[m Raio do cilindro : ')))
print(f'\033[32m>\033[m Volume do cilindro : {volume:.2f} un³')
