"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o 
recurso de mostrar que tipo de triângulo será formado:

EQUILÁTERO: todos os lados iguais

ISÓSCELES: dois lados iguais, um diferente

ESCALENO: todos os lados diferentes 
"""

print('-=-'*20)
print('\033[32m' + ' '*13 + '-----CALCULADOR DE TRIÂNGULOS-----' +'\033[0;0m')
print('-=-'*20)

l1 = int(input('Diga o comprimento do lado 1: '))
l2 = int(input('Diga o comprimento do lado 2: '))
l3 = int(input('Diga o comprimento do lado 3: '))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print('Pode ser triângulo')
    if l1 == l2 == l3:
        print('É equilátero. ')

    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('É isósceles. ')

    elif l1 != l2 != l3:
        print('É escaleno.')

else:
    print('Não pode ser um triângulo')


