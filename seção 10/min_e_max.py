"""
min e max

max() -> retorna o maior valor em um iterável ou o maior de dois ou mais elementos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = 1, 8, 4, 99, 34, 129
print(max(tupla))

set = {1, 8, 4, 99, 34, 129}
print(max(set))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))

nome = 'douglas'
print(max(nome))
"""

# Faça um programa que receba dois valores do usuário e mostre o maior:

'''
val1 = int(input('informe o primeiro valor: '))
val2 = int(input('informe o segundo valor: '))
val3 = int(input('informe o terceiro valor: '))
print(max(val1, val2, val3))
'''

''' ===================================================================== '''

'''
min() retorna o menor valor em um iterável ou o menor entre dois elementos.
'''

'''
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = 1, 8, 4, 99, 34, 129
print(min(tupla))

set = {1, 8, 4, 99, 34, 129}
print(min(set))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))

nome = 'douglas'
print(min(nome))
'''

''' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''
'''
nomes = ['douglas', 'tobias', 'erica maria']

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
'''

musicas = [
    {'titulo': 'musica1', 'quantidade': 3},
    {'titulo': 'musica2', 'quantidade': 2},
    {'titulo': 'musica3', 'quantidade': 20},
    {'titulo': 'musica4', 'quantidade': 1414}
]

print(max(musicas, key=lambda musica: musica['quantidade']))
print(min(musicas, key=lambda musica: musica['quantidade']))

## DESAFIO ##

# musica_mais_tocada = max(musicas, key=lambda musica: musica['quantidade'])
print(f'A música mais tocada foi a {max(musicas, key=lambda musica: musica["quantidade"])["titulo"]}.mp3'
      f' tocando incríveis {max(musicas, key=lambda musica: musica["quantidade"])["quantidade"]} vezes!!')
print(f'A música menos tocada foi a {min(musicas, key=lambda musica: musica["quantidade"])["titulo"]}'
      f' tocando apenas {min(musicas, key=lambda musica: musica["quantidade"])["quantidade"]} vezes')

'''UTILIZANDO O SORTED'''
print(f'A música menos tocada foi a {sorted(musicas, key=lambda musica: musica["quantidade"])[0]["titulo"]}'
      f' tocando apenas {min(musicas, key=lambda musica: musica["quantidade"])["quantidade"]} vezes')

print(f'A música mais tocada foi a {sorted(musicas, key=lambda musica: musica["quantidade"], reverse=True)[0]["titulo"]}'
      f' tocando incríveis {sorted(musicas, key=lambda musica: musica["quantidade"], reverse=True)[0]["quantidade"]} vezes!!')

min = 0
for musica in musicas:
    if min == 0:
        min = musica['quantidade']
    else:
        if musica['quantidade'] < min:
            min = musica['quantidade']
print(min)
