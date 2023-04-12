"""
Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo representará a operação que se
deseja efetuar com os números. Se o símbolo for + deverá ser realizada uma adição, se for - uma subtração,
/ para divisão e * para multiplicação.
"""


def calculadora(x, y, operador, mostra_eq=False):
    if operador == '+':
        if mostra_eq:
            return f'\033[34m  >\033[m {x} \033[34m+\033[m {y} = \033[34m{x + y}\033[m'
        else:
            return f'\033[34m  =\033[m {x + y}'
    elif operador == '-':
        if mostra_eq:
            return f'\033[34m  >\033[m {x} \033[34m-\033[m {y} = \033[34m{x - y}\033[m'
        else:
            return f'\033[34m  =\033[m {x - y}'
    elif operador == '/':
        if mostra_eq:
            return f'\033[34m  >\033[m {x} \033[34m/\033[m {y} = \033[34m{x / y}\033[m'
        else:
            return f'\033[34m  =\033[m {x / y}'
    elif operador == '*':
        if mostra_eq:
            return f'\033[34m  >\033[m {x} \033[34m*\033[m {y} = \033[34m{x * y}\033[m'
        else:
            return f'\033[34m  =\033[m {x * y}'
    else:
        return ''


def operador():
    while True:
        try:
            operador = str(input('  \033[32m[\033[37;1m   +    -    /    *    \033[m\033[32m]\033[m '
                                 '\033[37m[ 0 - sair ]\033[m \033[32m\n  >\033[m Operação : '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if operador == '0':
                print('  \033[31m> saindo <\033[m')
                return 0
            elif operador == '+':
                return '+'
            elif operador == '-':
                return '-'
            elif operador == '/':
                return '/'
            elif operador == '*':
                return '*'


def valor_x():
    while True:
        try:
            x = float(input('  \033[32m>\033[m x : '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            return x


def valor_y():
    while True:
        try:
            y = float(input('  \033[32m>\033[m y : '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            return y


print('-'.center(42, '-'))
print(' calculadora '.center(42, '-'))
print('-'.center(42, '-'))
while True:
    oper = operador()
    if oper == 0:
        break
    else:
        x = valor_x()
        print(f'  \033[34m{oper}\033[m')
        y = valor_y()
        if oper == '/' and y == 0:
            print('\033[31m  erro : valor inválido : divisão por ZERO\033[m')
            continue
        else:
            print(calculadora(x, y, oper))
            continue
