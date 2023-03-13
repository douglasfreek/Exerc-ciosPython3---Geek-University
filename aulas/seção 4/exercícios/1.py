while True:
    try:
        int = int(input('Digite um número inteiro: '))
    except:
        print('erro : digite um número inteiro')
    else:
        print(f'O número inteiro digitado foi {int}')
        break