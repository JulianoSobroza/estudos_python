"""
Exercício Python 37: Escreva um programa em Python que leia um
 número inteiro qualquer e peça para o usuário escolher qual
   será a base de conversão: 1 para binário, 2 para octal e 3 
   para hexadecimal. 
"""
print('CALCULADORA')
print('=-='*20)
numero = int(input('Digite um número qualquer: '))
print("""Você deseca converter para [B]inário, 
[O]ctal ou [H]exadecimal? """)
print('=-='*20)

conversao = input()
print('=-='*20)

if conversao == 'b':
    print('O numero em binário é: {}'.format(bin(numero)))
elif conversao == 'o':
    print('O número em octal é: {}'.format(oct(numero)))
elif conversao == 'h':
    print('o numero em hexadecimal é: {}'.format(hex(numero)))
else:
    print('Opção inválida.')

