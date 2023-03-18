"""
Escreva um programa de ajuda para vendedores.
A partir de um valor total lido, mostre:
- O total a pagar com desconto de 10%;
- O valor de cada parcela, no parcelamento de 3x sem juros;
- A comissão do vendedor para venda à vista (5% do valor com desconto);
- A comissão do vendedor, no caso da venda ser parcelada (5% sobre do valor total):
"""
while True:
    try:
        valor_venda = float(input('Valor total da venda: R$ '))
    except:
        print('\033[31merro : valor inválido\033[m')
    else:
        break

valor_desconto = valor_venda - (valor_venda / 100 * 10)
parcelado_tres = valor_venda / 3
comissao_vista = valor_desconto / 100 * 5
comissao_prazo = valor_venda / 100 * 5

print(f'Valor total da venda: R$ {valor_venda:.2f}')
print(f'Valor com desconto de 10%: R$ {valor_desconto:.2f}')
print(f'Valor da parcela em 3x: R$ {parcelado_tres:.2f}')
print(f'Comissão para venda à vista: R$ {comissao_vista:.2f}')
print(f'Comissão para venda à prazo: R$ {comissao_prazo:.2f}')