"""
Faça um programa que leia um número inteiro positivo de três digitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
NúmeroLido = 123
NúmeroGerado = 321
"""

while True:
    try:
        numero_lido = int(input('Digite um número de 100 a 999: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        if numero_lido < 100 or numero_lido > 999:
            print('\033[31merro : valor inválido\033[m')
            continue
        else:
            break

numero_str = str(numero_lido)
numero_gerado_str = numero_str[::-1]
print(f'Número digitado: {numero_lido}')
print(f'Número gerado: {numero_gerado_str}')
