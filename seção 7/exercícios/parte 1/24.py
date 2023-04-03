"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno
e o segundo representando a sua altura em metros.
Encontre o aluno mais baixo e o mais alto.
Mostre o número do aluno mais baixo e do mais alto, juntamente com suas alturas.
"""

alunos = {}
cod_menor = 0
for aluno in range(1, 11):
    while True:
        try:
            alunos[aluno] = float(input(f'Digite a altura do {aluno}º aluno: '))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break
    if cod_menor == 0:
        cod_menor = aluno
    elif alunos[aluno] < alunos[cod_menor]:
        cod_menor = aluno


print(f'O menor aluno mede \033[32m{alunos.get(cod_menor)}\033[m com o código: \033[32m{cod_menor}\033[m')
