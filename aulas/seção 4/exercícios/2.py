while True:
    try:
        real = float(input('Digite um número real: '))
    except:
        print('erro : digite um número real')
    else:
        print(f'O número real digitado foi {real:.2f}')
        break