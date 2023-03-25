"""
Faça um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior,
o menor e a média dos valores.
"""

valores = []
for n in range(5):
    while True:
        try:
            valores.append(float(input(f'Digite o {n + 1}º valor: ')))
        except:
            print('\033[31merro : valor inválido\033[m')
        else:
            break

print(f'Os valores digitados foram: \033[32m{valores}\033[m')
print(f'O maior valor digitado foi: \033[32m{max(valores)}\033[m')
print(f'O menor valor digitado foi: \033[32m{min(valores)}\033[m')
print(f'A média dos valores digitados foi: \033[32m{sum(valores) / len(valores)}\033[m')
