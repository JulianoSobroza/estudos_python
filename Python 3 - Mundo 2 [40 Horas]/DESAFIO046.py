"""
Exercício Python 46: Faça um programa que mostre na tela uma 
contagem regressiva para o estouro de fogos de artifício, indo
 de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
# função
from time import sleep
# codigo
for cont in range(10, -1, -1):
        #(comecça no 10)(-1 = 0)(passo = -1 para regressivo)
    sleep (0.3)
    print (cont)

print('POOOW PUM PARARAPUMM FIUUUUTCHUUUMM')