"""
Exercício Python 34: Escreva um programa que pergunte o salário
 de um funcionário e calcule o valor do seu aumento. Para 
 salários superiores a R$1250,00, calcule um aumento de 10%. 
 Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = int(input('Qual o valor do seu salário? '))
updez = salario + (salario *10/100)
upquinze = salario + (salario *15/100)

if salario > 1250:
    print ('Seu novo salário será de R${:.2f}'.format(updez))
else:
    print('Seu novo salário será de r${:.2f}'.format(upquinze))