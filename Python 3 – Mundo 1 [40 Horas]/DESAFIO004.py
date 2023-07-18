#DESAFIO 004

a = input('Digite algo aqui: ')  #uma função imput sempre retorna uma string, indeferente do tipo de valor inserido
print('O que você editou é do tipo: ', type(a))
print('Só tem espaços? ', a.isspace())
print(' é um número? ', a.isnumeric())
print( 'é alfabético? ', a.isalpha())