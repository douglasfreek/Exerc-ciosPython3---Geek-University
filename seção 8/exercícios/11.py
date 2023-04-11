"""
Elabore uma função que receba três notas de um aluno como parâmetros e uma letra.
Se a letra for A, a função deverá calcular a média aritmética das notas do aluno;
Se a letra for P, deverá calcular a média ponderada, com pesos 5, 3 e 2.
"""


def cat_notas():
    notas = []
    for n in range(1, 4):
        while True:
            try:
                nota = float(input(f'\033[32m>\033[m Valor da {n}ª nota \033[37m[ 0.0 a 10.0 ]\033[m : '))
            except:
                print('\033[31m erro : valor inválido\033[m')
            else:
                if nota > 10 or nota < 0:
                    print('\033[31m erro : valor inválido\033[m')
                    continue
                else:
                    notas.append(nota)
                    break
    return notas


def cat_letra():
    while True:
        try:
            letra = str(input('\033[32m>\033[m Qual média calcular? [ \033[32mA\033[m - Aritmética |'
                              '\033[32m P\033[m - Ponderada ] : '))[0].lower()
        except:
            print('\033[31m erro : valor inválido\033[m')
        else:
            if letra not in 'pa':
                print('\033[31m erro : valor inválido\033[m')
            else:
                if letra == 'a':
                    return 'a'
                else:
                    return 'p'


def media(*args, let='a'):
    n1, n2, n3 = args[0]
    n1 *= 5
    n2 *= 3
    n3 *= 2
    soma = n1 + n2 + n3
    if let == 'a':
        return sum(args[0]) / len(args[0])
    else:
        return soma / 10


print('-'.center(45, '-'))
print(' calculadora de médias '.center(45, '-'))
print('-'.center(45, '-'))
notas = cat_notas()
tipo_media = cat_letra()
if tipo_media == 'a':
    print(f'\033[32m>\033[m Média aritimética de \033[32m{notas}\033[m = \033[32m{media(notas, tipo_media):.1f}\033[m')
else:
    print(f'\033[32m>\033[m Média ponderada de \033[32m{notas}\033[m = \033[32m{media(notas, tipo_media):.1f}\033[m')
