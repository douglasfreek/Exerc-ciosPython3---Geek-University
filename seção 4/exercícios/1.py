while True:
    try:
        inteiro = int(input('Digite um número inteiro: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        print(f'O número inteiro digitado foi {int}')
        break