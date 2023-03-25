"""
Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro.
Se o código for 0, finalize o programa; se for 1, mostre o vetor na ordem direta; se for 2, mostre na ordem inversa.
Caso o código seja diferente de 1 e 2, escreva uma mensagem informado o erro.
"""
numeros = []
for n in range(5):
    while True:
        try:
            numeros.append(float(input(f'Digite o {n + 1}º número: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break
print('\n')
while True:
    print('-=-' * 7)
    print(f'{"MENU":^21}')
    print('-=-' * 7)
    print('''[ 1 ] Mostrar vetor
[ 2 ] Inverter vetor
[ 0 ] Sair''')
    try:
        opcao = int(input('\033[32m>\033[m opção : '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if opcao == 1:
            print()
            print(f'\t\033[32m>\033[m Vetor = {numeros}\n')
        elif opcao == 2:
            print()
            numeros.reverse()
            print(f'\t\033[32m>\033[m Vetor invertido = {numeros}\n')
        elif opcao == 0:
            break
        else:
            print('\033[31merro : valor inválido\033[m')
            continue
