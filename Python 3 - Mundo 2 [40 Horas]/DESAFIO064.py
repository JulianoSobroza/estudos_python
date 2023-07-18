"""
Exercício Python 064: Crie um programa que leia vários números inteiros pelo 
teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a 
condição de parada. No final, mostre quantos números foram digitados e qual foi 
a soma entre eles (desconsiderando o flag).
"""

n = ''
contador = 0
n1 = 0
n2 = 0
print('CONTADOR DE NÚMEROS INTEIROS')
print('[digite 999 para encerrar]')
while n != 999:
    n = int(input('Digite um número inteiro: '))
    n1 +=n
    contador += 1
    if n == 999:
      print('Você digitou {} números e a soma deles é {}'.format((contador-1), (n1 - 999)))
    else:
      print(n1)
   
   
