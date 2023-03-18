"""
Faça um programa para converter uma letra maiúscula em letra minúscula.
Use a tabela ASCII para resolver o problema:
"""

while True:
    letra_maiuscula = str(input('Digite alguma letra em CAIXA ALTA: ')).strip()
    if letra_maiuscula.islower() or letra_maiuscula.isnumeric() or letra_maiuscula == '' or len(letra_maiuscula) > 1:
        print('\033[31merro : valor inválido\033[m')
        continue
    else:
        break

ord_maiuscula = ord(letra_maiuscula)
ord_minuscula = ord(letra_maiuscula.lower())
minuscula = chr(ord_minuscula)
print(f'Letra digitada em caixa baixa: {minuscula}')
