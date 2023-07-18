"""
Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e
 mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
"""

from time import sleep
# caceçalho
print(('▲▼')*30)
sleep(0.3)
print('{:=^60}'.format(' SEQUÊNCIA DE FIBONACCI '))
print('')
sleep(0.5)
print('  '*20 +'By: JBS tecnologias.')
sleep(0.3)
print(('▲▼')*30)
print(' ')
sleep(0.7)



ntermos = int(input('Diga quantos termos: '))
contador = 3
n1 = 0
n2 = 1
print('{} → {}'.format(n1, n2), end='')

while contador <= ntermos:
    n3 = n2 + n1
    print(' → {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    contador +=1

print(' → FIM.')

# rodapé
print(('▲▼')*30)
print('')
sleep(0.5)
print('  '*17 +'Obrigado pela preferência.')
sleep(0.3)
print(('▲▼')*30)