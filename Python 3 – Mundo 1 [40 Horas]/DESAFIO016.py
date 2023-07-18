# crie um prog que leia um n real qualquer e mostre na tela sua porção inteira 
# ex; digitar 1.125 e aparecer 1

#import math     #importa todas as funcionalidades da biblioteca math
from math import trunc      #importa somente a função truncate
num = float(input('Digite um valor: '))     
print ('O valor digitado é {} e porção inteira é {}.'.format(num, math.trunc(num)))

#math.trunc pega o valor abaixo
#matg.floor pega o valor com virgula
