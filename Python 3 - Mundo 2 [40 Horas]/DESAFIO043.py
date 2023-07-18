"""
Exercício Python 43: Desenvolva uma lógica que leia o peso 
e a altura de uma pessoa, calcule seu Índice de Massa Corporal 
(IMC) e mostre seu status, de acordo com a tabela abaixo:

 IMC abaixo de 18,5: Abaixo do Peso

 Entre 18,5 e 25: Peso Ideal

 25 até 30: Sobrepeso

 30 até 40: Obesidade

 Acima de 40: Obesidade Mórbida 
"""
# funções
from time import sleep

# cabeçalho
print(('-=-')*20)
sleep(0.5)
print(' '*15 +'-----CALCULADORA DE IMC-----' + ' '*15)
print('')
sleep(0.5)
print('  '*15 +'Powered by: JBS tecnologias.')
sleep(0.5)
print(('-=-')*20)
sleep(2)

# dados
peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))
print (' ')
sleep(2)

# cálculo
imc = peso / altura**2
print('Seu imc é {:.2f}'.format(imc))
sleep(1)
print(' ')
print('Sua classificação de IMC é: ')
sleep(1)

# lógica
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 < imc <= 25:
    print('Peso ideal.')
elif 25 < imc <= 30:
    print('Sobrepeso.')
elif 30 < imc <= 40:
    print('Obesisdade.')
elif 40 < imc:
    print('Obesidade mórbida.')

print(' ')
print(('-=-')*20)

