"""
Leia quatro notas, calcule a média aritmética e imprima o resultado:
"""

cont = 1
notas = []

while True:
    try:
        notas.append(float(input(f'Digite a nota do {cont}º bimestre: ')))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        cont += 1
        if cont > 4:
            break

media = sum(notas) / 4
cont = 1

for nota in notas:
    print(f'{cont}º Bimestre: {nota:.2f}')
    cont += 1

print(f'A média final é igual a {media:.2f}')
