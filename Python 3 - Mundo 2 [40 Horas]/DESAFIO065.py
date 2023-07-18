"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo 
teclado. No final da execução, mostre a média entre todos os valores e qual 
foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se
 ele quer ou não continuar a digitar valores.
"""
resp = 'S'
soma = quant = média = maior = menor = 0 #assim todas recebem 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = (soma / quant)
print('A média de todos os valores é {}. Foi digitado um total de {} números'.format(média, quant))