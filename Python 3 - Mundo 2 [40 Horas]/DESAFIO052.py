"""
Exercício Python 052: Faça um programa que leia um número inteiro e diga se
 ele é ou não um número primo.
"""
#Um número primo é aquele que é dividido apenas por um e por ele mesmo.

n = int(input('Digite um número: '))

for c in range (1, n+1):
    if n % c ==0:
        #print('{} é primo.'.format(n))
        print('\033[34m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')