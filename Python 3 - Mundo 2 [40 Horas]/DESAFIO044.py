"""
Exercício Python 44: Elabore um programa que calcule o valor a
 ser pago por um produto, considerando o seu preço normal e 
 condição de pagamento:

à vista dinheiro/cheque: 10% de desconto

à vista no cartão: 5% de desconto

em até 2x no cartão: preço formal 

3x ou mais no cartão: 20% de juros
"""
# funções
from time import sleep

# caceçalho
print(('-=-')*20)
sleep(0.3)
print('{:=^60}'.format(' LOJAS SOBROZA '))
print('')
sleep(0.5)
print('  '*20 +'By: JBS tecnologias.')
sleep(0.3)
print(('-=-')*20)
print(' ')
sleep(0.7)

# entrada
preco = float(input('Valor do produto: R$'))
print (' ')
sleep(0.3)
print('Qual a forma de pagamento? ')
print(' ')
sleep(0.3)
print('[1] à vista dinheiro/cheque: 10% de desconto')
sleep(0.3)
print('[2] à vista no cartão: 5% de desconto')
sleep(0.3)
print('[3] em até 2x no cartão: preço normal ')
sleep(0.3)
print('[4] 3x ou mais no cartão: 12% de juros')
print(' ')
condicao = (input(''))

# lógica
if condicao == '1':
    print('Pagamento: R${:.2f}'.format(preco - preco*(10/100)))

elif condicao == '2':
    print('Pagamento: R${:.2f}'.format(preco - preco*(5/100)))
elif condicao == '3':
    print('Pagamento em duas vezes de: R${:.2f}'.format(preco/2))
elif condicao == '4':
    print('Pagamento em três vezes de: R${:.2f}'.format((preco + preco*(12/100))/3))

print(' ')
print(('-=-')*20)

