"""
Faça um algoritmo utilizando o comando while que mostra um contagem regressiva na tela
iniciando em 10 e terminando em 0.
Mostrar um mensagem FIM após a contagem.
"""

contador = 11

while contador > 0:
    contador -= 1
    print(contador, end=' ')
    if contador == 0:
        print('', end='FIM')
