"""
Exercício Python 28: Escreva um programa que faça o computador
 “pensar” em um número inteiro entre 0 e 5 e peça para o 
 usuário tentar descobrir qual foi o número escolhido pelo 
 computador. O programa deverá escrever na tela se o usuário
   venceu ou perdeu.
"""
import random # toda a biblioteca dos randomicos
from time import sleep # função que da um intervalo de tempo na execução dos códigos

aleatorio = (random.randint(0, 5)) #o pc vai escolher um número randomico, entre parênteses é o intervalo de escolha
print('-=-' *25) #enfeite
print('Eu escolhi um número entre 0 e 5. Tente adivinhar qual é.')
sleep(2)
print('-=-' *25) #enfeite

user = int(input('Diga o número: ')) # o usuário vai chutar um valor
print('-=-' *25) #enfeite

print('PROCESSANDO...')
sleep(2)
print('-=-' *25) #enfeite

if aleatorio == user:
    print('Você acertou, o número é: {}'. format(aleatorio))
else:
    print('Você errou, try again.')
    sleep(1.2)
    print('Eu havia escolhido o número {} :)'.format(aleatorio))

print('-=-' *25) #enfeite




