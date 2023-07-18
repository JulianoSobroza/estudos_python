"""
Exercício Python 39: Faça um programa que leia o ano de 
nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora 
exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que 
passou do prazo.
"""
import	datetime

today = datetime.date.today()
ano = today.year

nascimento = int(input('Que ano você nasceu? '))
idade = (ano - nascimento)

faltam = 17 - idade

if idade == 17:
    print('Você precisa se alistar nesse ano.')

elif idade >= 18:
    print('Você passou do prazo de alistamento')

elif idade <= 16:
    print('Você ainda tem que esperar {} anos para se alistar'.format(faltam))
