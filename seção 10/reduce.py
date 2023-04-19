"""
Reduce

A partir da versão 3 do python o reduce deixou de ser uma função integrada, ou built-in
Para utilizar a função reduce devemos importar da biblioteca functools

Guido van Rossum: Na maioria dos casos a função reduce pode ser substituída por um loop for

# entendendo o reduce :

imagine que você tenha uma coleção de dados:

dados = [a1, a2, a3, ..., an]

e uma função que receba dois parâmetros:

def funcao(x, y):
    return x * y

assim como map() e filter() a função reduce recebe dois parâmetros: função e um iterável

reduce(funcao, iteravel)

reduce vai funcionar da seguinte forma:
    passo 1: res1 = f(a1, a2)
        - reduce vai aplicar a função nos dois primeiros elementos do iterável e vai guarda o resultado:
    passo 2: res2 = f(res1, a3)
        - no segundo passo a função vai utilizar o resultado gerado no primeiro passo como primeiro parâmetro, e o terceiro elemento como segundo parâmetro
    passo 3: res3 = f(res2, a4)
        - a função reduce fará isso com todos os elementos do iterável, acumulando os resultados que já foram calculados até calcular com todos os elementos do iterável.

"""
from functools import reduce


def func(x, y):
    return x + y


def multi(x, y):
    return x * y


numeros = [1, 2, 3, 4, 5, 6, 8]
print(reduce(func, numeros))
print(reduce(multi, numeros))

# 1 + 2 = 3 ---> 3 + 3 = 6 ---> 6 + 4 = 10 ---> 10 + 5 = 15
# a função reduce somou os dois primeiros elementos, o resultado somou com o terceiro, o resultado somou com o quarto elemento e assim até somar todos os elementos
# o resultado de reduce é numérico, não precisa cast

resultado = 1
for n in numeros:
    resultado *= n
print(resultado)
# o reduce() funciona como um loop for dentro do iterável
# a função para ser utilizada no reduce() SEMPRE deverá receber DOIS PARÂMETROS



