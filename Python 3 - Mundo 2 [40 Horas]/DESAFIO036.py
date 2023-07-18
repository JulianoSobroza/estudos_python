"""
Exercício Python 36: Escreva um programa para aprovar o 
empréstimo bancário para a compra de uma casa. Pergunte o
 valor da casa, o salário do comprador e em quantos anos ele
   vai pagar. A prestação mensal não pode exceder 30% do 
   salário ou então o empréstimo será negado.
"""

valorcasa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o salário do comprador? '))
tempo = int(input('Deseja pagar em quantos anos? '))

prestacao = valorcasa/(tempo*12)

#prestacao = valorcasa/totalparcelas
#totalparcelas = (valorcasa/(tempo*12))

if prestacao > salario*(30/100):
    print('O empréstimo foi negado.')

else:
    print('O empréstimo foi aprovado. Seu valor será de R${} mensais por um total de {} parcelas./'.format(prestacao, tempo*12))
           
           


#print('total parcela é {} meses.'.format(totalparcelas))


