"""
Exercício Python 33: Faça um programa que leia três números
 e mostre qual é o maior e qual é o menor.
"""
# nunca copie e cole quando se está aprendendo

n1 = int(input('primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

# verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n2:
    menor = n3
# verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor digitado foi {}'.format(menor))
print('O mmaior valor digitado foi {}'.format(maior))
