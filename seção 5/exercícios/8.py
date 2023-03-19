"""
Faça um programa que leia duas notas de um aluno, verifique se as notas são válidas e exiba na tela
a média dessas notas.
Uma nota válida deve ser, obrigatoriamente, um valor enter 0.0 e 10.0, onde, caso a nota não possua um valor válido,
este fato deve ser informado ao usuário e o programa termina.
"""

while True:
    try:
        nota_1 = float(input('Digite a primeira nota: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if nota_1 < 0 or nota_1 > 10:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            break

while True:
    try:
        nota_2 = float(input('Digite a segunda nota: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if nota_2 < 0 or nota_2 > 10:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            break

print(f'A primeira nota foi {nota_1:.2f} e a segunda nota foi {nota_2:.2f}')
print(f'A média é igual a {(nota_1 + nota_2) / 2:.2f}')
