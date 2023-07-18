"""
Exercício Python 31: Desenvolva um programa que pergunte a 
distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
 parta viagens mais longas.
"""

dist = int(input('Distância em Km: ')) 
menor = dist * 0.5
maior = dist * 0.45

if dist <= 200:
    print('O preço da passagem será de R${:.2f}'.format(menor))
else:
    print('O preço da passagem será de R${:.2f}'.format(maior))
