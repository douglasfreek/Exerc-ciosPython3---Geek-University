while True:
    try:
        real = float(input('Digite um número real: '))
    except:
        print('\033[31merro : digite um número inteiro\033[m')
    else:
        print(f'O número real digitado foi {real:.2f}')
        break