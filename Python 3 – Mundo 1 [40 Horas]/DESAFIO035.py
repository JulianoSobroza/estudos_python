"""
Exercício Python 35: Desenvolva um programa que leia o 
comprimento de três retas e diga ao usuário se elas podem 
ou não formar um triângulo.
"""
"""
"Dados três segmentos de reta distintos, se a soma das medidas
 de dois deles é sempre maior que a medida do terceiro, então,
   eles podem formar um triângulo."

"""

r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Pode ser um triângulo.')
else:
    print('Não pode ser um triângulo.')


