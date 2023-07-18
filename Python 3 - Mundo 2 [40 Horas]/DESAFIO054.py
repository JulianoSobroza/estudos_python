"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
 maiores.
"""
import datetime
today = datetime.date.today()
anoatual = today.year

totmaior = 0
totmenor = 0

for c in range(1, 8):
    ano = int(input('Que ano a {}º pessoa nasceu? '.format(c)))
    idade = anoatual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor =+ 1
print('Ao todo temos {} pessoas menores de idade.' .format(totmenor))
print('E tivemos {} pessoas maiores de idade.'.format(totmaior))