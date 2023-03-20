"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 a 10,
respectivamente, a um trabalho de laboratório, uma avaliação semestral e um exame final.
A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de laboratório, peso 2;
Avaliação semestral, peso 3; Exame final, peso 5.
De acordo com o resultado mostre na tela a situação do aluno:
    - Média entre 0.0 e 2.9 = Reprovado
    - Média entre 3.0 e 4.9 = Recuperação
    - Média 5 ou mais = Aprovado
"""
notas = []
for n in range(0, 3):
    while True:
        try:
            if n == 0:
                n = 'Trabalho de Laboratório, peso 2'
            elif n == 1:
                n = 'Avaliação Semestral, peso 3'
            elif n == 2:
                n = 'Exame Final, peso 5'
            notas.append(float(input(f'Digite a nota do \033[34m{n}\033[m: [0.0 a 10.0] = ')))
            if n == 'Trabalho de Laboratório, peso 2':
                n = 0
            elif n == 'Avaliação Semestral, peso 3':
                n = 1
            elif n == 'Exame Final, peso 5':
                n = 2
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            if notas[n] < 0 or notas[n] > 10:
                print('\033[31merro : valor inválido\033[m')
                del notas[n]
                continue
            else:
                break

media = ((notas[0] * 2) + (notas[1] * 3) + (notas[2] * 5)) / 10  # 10 é a soma de todos os pesos
print(f'Trabalho de laboratório: {notas[0]:.1f} x peso 2 = {notas[0] * 2}')
print(f'Avaliação semestral: {notas[1]:.1f} x peso 3 = {notas[1] * 3}')
print(f'Exame final: {notas[2]:.1f} x peso 5 = {notas[2] * 5}')
print(f'MÉDIA FINAL = {media:.1f}')
