"""
Exercício Python 030: Crie um programa que leia um número
 inteiro e mostre na tela se ele é PAR ou ÍMPAR
"""

numero = int(input('Digite um número qualquer: '))

#operadores

resultado = numero % 2 #o resto da divisão por 2
# o resto da divisão por dois que qualquer par é 0
# o resto da divisão por dois que qualquer impar é 1

if resultado !=0:
    print('O número é impar.')

else:
    print('O número é par.')