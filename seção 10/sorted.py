"""
sorted()

também é uma função integrada (built-in)

apesar do nome, não confundir com a função sort(), utilizada em listas
o sort() só funciona em listas

já o sorted() podemos utilizar com qualquer iterável
sorted() serve para ordenar os elementos dentro do iterável
"""


'''lista = [5, 78, 4, 0]
print(lista)
lista.sort()  # o sort() ele modifica a lista original, a partir desse momento, o objeto passará a ser sempre sort
print(lista)
print(lista)
'''
# a função sort() só funciona em listas
# a sorted() em qualquer iterável

'''listas = (1, 2, 3, 4, 8, 9, 1, 0, 0, 2)
print(listas)
print(sorted(listas))  # o sorted() não modifica a lista original, ela continua intacta, ele gera uma nova listas ordenada para retornar
print(listas)  # *** obs *** o sorted() sempre retorna o iterável ordenado em uma LISTA
               # mesmo se o objeto original for uma tupla, o sorted() retornará uma lista
'''
'''print('=' * 50)
listas = (1, 2, 3, 4, 8, 9, 1, 0, 0, 2)
print(sorted(listas))  # lista ordenada
print(sorted(listas, reverse=True))  # lista ordenada e invertida
print(tuple(sorted(listas)))  # convertendo para retornar uma tupla -> cast
'''
'''
podemos utilizar o sorted() para coisas mais complexas, por exemplo:
'''
'''
usuarios = [
    {'username': 'samuel', 'tweets': ['eu adoro bolos', 'eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['eu gosto de cachorros', 'vou sair hoje']},
    {'username': 'gal', 'tweets': []}
]

for usuario in usuarios:
    print(usuario)

print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario['username']))  # key está retornando por qual item do dicionário a lista será ordenada, nesse caso, 'username':
print(sorted(usuarios, key=lambda x: x['tweets']))  # nesse caso, a lista está sendo ordenada pela chave 'tweets', em ordem alfabetica pela primeira letra de cada tweet
print(sorted(usuarios, key=lambda x: len(x['tweets'])))  # nesse caso, está ordenando pela quantidade de tweets dentro da key['tweets']
'''

musicas = [
    {'titulo': 'musica1', 'quantidade': 3},
    {'titulo': 'musica2', 'quantidade': 2},
    {'titulo': 'musica3', 'quantidade': 4},
    {'titulo': 'musica4', 'quantidade': 32}
]

print(sorted(musicas, key=lambda musica: musica['quantidade']))
print(sorted(musicas, key=lambda musica: musica['quantidade'], reverse=True))
