"""
Escreva um função que receba um número inteiro maior do que zero e retorne a soma de todos os seus algarismos.
Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1)
Se o número lido não for maior que zero, o programa terminará com a mensagem 'número inválido'
"""


def soma_numeros(numero, show_eq=False):
    """
    -> Recebe uma lista de valores inteiros maior que zero e retorna a soma de seus algarismos
    :param numero: número inteiro maior que zero
    :param show_eq: True mostra a equação da soma de todos os algarismos
    :return: retorna soma de todos os algarismos do número inteiro
    """
    str_num = str(numero)
    if show_eq:
        for x, n in enumerate(str_num):
            if x < len(str_num) - 1:
                print(f'{n}', end=' + ')
            else:
                print(f'{n} = ', end='')
    return sum(int(num) for num in str_num)


while True:
    try:
        num = int(input('\033[32m>\033[m Digite um número inteiro positivo \033[37m[ 0 - sair ]\033[m : '))
    except:
        print('\033[31m erro : valor inválido\033[m')
    else:
        if num < 0:
            print('\033[31m erro : valor inválido\033[m')
        elif num == 0:
            print('\033[31m> saindo... <\033[m')
            break
        else:
            print(f'\033[32m{soma_numeros(num, True)}\033[m')
