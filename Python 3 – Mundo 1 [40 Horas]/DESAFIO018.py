"""
Faça um programa que leia um ângulo qualquer e mostre na 
tela o valor do seno, cosseno e tangente desse ângulo.

"""
import math

valor_angulo_em_graus = int(input('Diga o valor do ângulo: '))

sen = math.sin (math.radians(valor_angulo_em_graus)) #math.radians para ler o valor em graus
cos = math.cos (math.radians(valor_angulo_em_graus))
tg = math.tan (math.radians(valor_angulo_em_graus))

print('Os valores de sen cos e tg são respec\
tivamente {:.2f}, {:.2f}, e {:.2f}'.format (sen, cos, tg))