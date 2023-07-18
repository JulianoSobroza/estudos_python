"""
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de
 uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print('→→→→→ CALCULADORA DE PA v2.0 ←←←←←')

primeiro = int(input('Diga o primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print(' FIM.')