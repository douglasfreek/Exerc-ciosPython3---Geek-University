"""
A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso,
sendo que da quantia total:
- O primeiro ganhador receberá 46%
- O segundo receberá 32%
- O terceiro recebera o restante
"""

premio_total = 780000
primeiro = premio_total / 100 * 46
segundo = premio_total / 100 * 32
terceiro = premio_total / 100 * (100 - 46 - 32)
print(f'Prêmio total: R$ {premio_total:.2f}')
print(f'\t- O primeiro ganhador receberá 46% = R$ {primeiro:.2f}')
print(f'\t- O segundo ganhador receberá 32% = R$ {segundo:.2f}')
print(f'\t- O terceiro ganhador receberá {100 - 46 - 32}%  = R$ {terceiro:.2f}')
