while True:
    try:
        numero = float(input('Digite um número real: '))
    except:
        print('erro : digite um número real')
    else:
        print(f'O quadrado de {numero:.2f} é igual a {numero ** 2:.2f}')
        break
