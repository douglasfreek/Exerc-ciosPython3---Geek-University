"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova tem peso 1 e a terceira prova tem peso 2.
Ao final, mostrar a média e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

notas = []

for nota in range(1, 4):
    while True:
        try:
            notas.append(float(input(f'Digite a {nota}ª nota [0.00 a 100.00]: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if notas[nota - 1] > 100:
                del notas[nota - 1]
                print('\033[31merro : valor inválido\033[m')
                continue
            if nota == 3:
                notas[2] = notas[2] * 2
                break
            else:
                break

media = sum(notas) / 4
print(f'A primeira, segunda e terceira nota, respectivamente, foram {notas}. Com peso 2 na terceira nota.')
print(f'A média ponderada das três notas é igual a {media:.2f}')
if media >= 60:
    print('Resultado final: \033[32mAPROVADO\033[m')
else:
    print('Resultado final: \033[31mREPROVADO\033[m')