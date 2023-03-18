"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
"""

while True:
    try:
        altura_degrau = float(input('Digite a altura do degrau da escada, em metros: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

while True:
    try:
        altura_escada = float(input('Digite a altura total da escada, em metros: '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

quant_degraus = altura_escada / altura_degrau
print(f'Serão necessários {quant_degraus:.0f} degraus para altura correta.')
