"""
Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão
 de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
#an = a1 + (c - 1)*r
#décimo termo de uma PA para o segundo jeito de fezer
a10 = a1 + (10-1) * r

#primeiro jeito
# for c in range (1, 11):
#     print(a1 + (c - 1)*r, end=' → ',)
# print('ACABOU')

#segundo jeito
for c in range (a1, a10 + r, r):
    print(c, end=' → ',)
print('ACABOU')
