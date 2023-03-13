while True:
    try:
        numero = float(input('Digite um número real: '))
    except:
        print('erro : digite um número real')
    else:
        print(f'A quinta parte de {numero:.2f} é igual a {numero / 5:.2f}')
        break