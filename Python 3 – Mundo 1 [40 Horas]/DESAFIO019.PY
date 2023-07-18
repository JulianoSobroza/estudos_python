
"""
Um professor quer sortear um dos seus quatro alunos para apagar 
o quadro. Faça um programa que ajude ele, lendo o nome dos 
alunos e escrevendo na tela o nome do escolhido.
"""

from random import choice #importando o randomizador

aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4] #listas em python
escolhido = choice(lista) #choice é o escolhedor


print('O aluno escolhido é {}'. format(escolhido))