"""
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele
 quer mostrar mais alguns termos. O programa encerrará quando ele disser que
 quer mostrar 0 termos.
"""

print('→→→→→ CALCULADORA DE PA v3.0 ←←←←←')

primeiro = int(input('Diga o primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print(' FIM.')