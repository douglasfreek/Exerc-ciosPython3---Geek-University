"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.
"""

alunos_e_notas = {}
total = 0
media = total / len(alunos_e_notas)

while True:
    try:
        quantidade = int(input('Quantos alunos deseja cadastrar? '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break
while not len(alunos_e_notas) == quantidade:
    nome = str(input('Nome do aluno: ')).strip().title()
    if nome in alunos_e_notas.keys():
        print('\033[31merro : aluno já cadastrado\033[m')
    elif nome == '' or nome.isnumeric():
        print('\033[31merro : valor inválido\033[m')
    else:
        try:
            alunos_e_notas[nome] = float(input('Nota: '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if alunos_e_notas[nome] > 10 or alunos_e_notas[nome] < 0:
                del alunos_e_notas[nome]
                print('\033[31merro : valor inválido\033[m')
            else:
                pass
print('-=-' * 18)
for nome, nota in sorted(alunos_e_notas.items()):
    print(f'\033[32mALUNO\033[m: {nome:<30} | \033[32mNOTA\033[m: {nota:<5.2f}')
    total += nota
print('-=-' * 18)
print(f'MÉDIA GERAL: \033[32m{media:.2f}\033[m\n')
