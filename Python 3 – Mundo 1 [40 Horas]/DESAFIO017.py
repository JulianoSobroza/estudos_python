# Faça um programa que leia o compromento do CO e do CA de um
#triangulo retângulo, calcule e mostre o comprimento da H.

c1 = float(input('Comprimento do CO: '))
c2 = float(input('Comprimento do CA: '))
h = (c1 ** 2 + c2 ** 2) ** (1/2)
print('O comprimento da Hipotenusa é: {:.3f}' .format(h))