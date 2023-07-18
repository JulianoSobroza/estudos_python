"""
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

 O nome com todas as letras maiúsculas e minúsculas.
 Quantas letras ao todo (sem considerar espaços).
 Quantas letras tem o primeiro nome.
"""

# nome = str(input('Digite seu nome completo: ')).strip #deixar explicito que é uma string                              
# print('Analisando seu nome...')
# print(f'Seu nome em maiúsculo é {}'.format{nome.upper()})
# print(f'Seu nome emminúsculo é {}'.format{nome.lower()})
# print(f'Seu nome possui um total de {} letras'.format(len(nome)-nome.count(' ')))


nome = str(input('Digite o seu nome completo: ')).strip()

print('Analisando seu nome...')

print(f'Seu nome completo em maiusculas é {nome.upper()}')

print(f'Seu nome completo em minusculas é {nome.lower()}')

espacos = (nome.count(' '))

print(f'Seu nome tem ao todo {len(nome) - espacos} letras')

primeiro = nome.find(' ')

print(f'Seu primeiro nome tem {primeiro} letras.')

