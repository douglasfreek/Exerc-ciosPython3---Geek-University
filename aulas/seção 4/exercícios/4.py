while True:
    try:
        numero = float(input('Digite um número real: '))
    except:
        print('\033[31merro : digite um número inteiro\033[m')
    else:
        print(f'O quadrado de {numero:.2f} é igual a {numero ** 2:.2f}')
        break
