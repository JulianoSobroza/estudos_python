"""
Exercício Python 050: Desenvolva um programa que leia seis números
 inteiros e mostre a soma apenas daqueles que forem pares. Se o valor 
 digitado for ímpar, desconsidere-o.
"""
from time import sleep
# caceçalho
print(('-=-')*20)
sleep(0.3)
print('{:=^60}'.format(' SOMADOR DE PARES '))
print('')
sleep(0.5)
print('  '*20 +'By: JBS tecnologias.')
sleep(0.3)
print(('-=-')*20)
print(' ')
sleep(0.7)

#declarando variaveis
soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite {}º valor: '.format(c)))
    if num % 2 == 0:
        soma = num + soma
print('A soma dos números pares é {}'.format(soma))

# rodapé
print(('-=-')*20)
sleep(0.3)
print('{:=^60}'.format(' FIM. '))
print('')
sleep(0.5)
print('  '*15 +'Obrigado pela preferência.')
sleep(0.3)
print(('-=-')*20)