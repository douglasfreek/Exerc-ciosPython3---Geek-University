"""
Leia a altura e o raio de um cilíndro circular e imprima o volume do cilindro.
fórmula: V = π * raio² * altura
π = 3.141592
"""
while True:
    try:
        altura = float(input('Digite a altura do cilíndro: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

while True:
    try:
        raio = float(input('Digite o raio do cilíndro: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

volume = 3.141592 * raio ** 2 * altura
print(f'O volume do cilindro em questão é de {volume:.2f} un³')
