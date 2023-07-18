"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se 
ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
 ANOTARAM A DATA DA MARATONA.
"""
#entrada #tem que saber sobre tratamentos de string
frase = str(input('Digite sua frase aqui: ')).strip().upper() #(eliminou espaços antes e depois, jogou pra maiusculo)
palavras = frase.split() #dividindo as palavras (separando)
tudojunto = ''.join(palavras) # eliminou espaços internos (e se colocar * dentro do''?)
inverso = '' # vazio no inicio

for letra in range(len(tudojunto) - 1, -1, -1):
# len → vai pegar o nº de letras do junto e vai tirar 1,
# vai até a letra -1(antes da primeira)
# e vai voltando uma letra
    #print('Você digitou a frase: {}'.format(tudojunto[letra]))
    inverso += tudojunto [letra]

print(tudojunto, inverso)
