"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do 
programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
 e quantas mulheres têm menos de 20 anos.
"""

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range (1 , 5):
    print('-'*5 + ' {}ª PESSOA '.format(p) + '-'*5)
    nome = str(input('Nome: ')).strip() #strip tira os espaços antes/dps da palavra
    idade = int(input('Idade: '))
    somaidade += idade
    sexo = str(input('Sexo [M/F]: ')).strip()
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('A idade média é de {} anos.'.format(mediaidade))
print('O homem mais venho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))