"""
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai 
"pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
 até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

import random

aleatorio = (random.randint(0, 11))
print('Acabei de pensar em um número entre 0 e 10.')
acertou = False
palpite = 0
while not acertou:
    chute = int(input('Quer tentar adivinhar? Diga um número: '))
    palpite += 1
    if aleatorio == chute:
        acertou = True
    elif chute > aleatorio:
        print('É menor.')
    elif chute < aleatorio:
        print('É maior.')
print('Acertou com um total de {} tentativas!'.format(palpite))
