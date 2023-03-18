"""
Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha:
"""

while True:
    try:
        numero_int = int(input('Digite um número inteiro de 1000 a 9999: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if numero_int < 1000 or numero_int > 9999:
            print('\033[31merro : valor inválido\033[m')
        else:
            numero_str = str(numero_int)
            break

for n in numero_str:
    print(f'{n}')
