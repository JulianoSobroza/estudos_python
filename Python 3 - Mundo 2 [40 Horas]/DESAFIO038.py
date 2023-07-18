"""
Exercício Python 038: Escreva um programa que leia dois números 
inteiros e compare-os. mostrando na tela uma mensagem:

 O primeiro valor é maior

 O segundo valor é maior

 Não existe valor maior, os dois são iguais
"""
print('-=-'*20)
print('\033[32m' + ' '*13 + '-----COMPARADOR DE NÚMEROS-----' +'\033[0;0m')
print('-=-'*20)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O primeiro é maior.')
elif n1 < n2:
    print('O segundo número é maior.')
elif n1 == n2:
    print('Os números são iguais.')
else:
    print('Digite um número válido.')

print('-=-'*20)
print('\033[32m' + ' '*8 + '-----OBRIGADO POR USAR O NOSSO PRODUTO-----' +'\033[0;0m')
print('-=-'*20)
