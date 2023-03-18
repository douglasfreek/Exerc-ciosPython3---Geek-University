while True:
    try:
        numero = float(input('Digite um número real: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        print(f'A quinta parte de {numero:.2f} é igual a {numero / 5:.2f}')
        break