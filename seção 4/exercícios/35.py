"""
Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação e imprima o resultado.
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = √ a² + b²    ->     (√ -> raiz quadrada)
"""
while True:
    try:
        a = float(input('Digite o valor do cateto "a": '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

while True:
    try:
        b = float(input('Digite o valor do cateto "b": '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        hipotenusa = ((a ** 2) + (b ** 2)) ** 0.5
        print(f'A raíz da soma dos quadrados dos catetos {a} e {b} é igual a hipotenusa {hipotenusa:.2f}.')
        break
