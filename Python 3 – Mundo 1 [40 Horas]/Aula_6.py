##Aula 6 – Tipos Primitivos e Saída de Dados
# int = 7, 55, 0, 9000
# float = 7.5, 2.244652, -0.33, 7.0
# bool = True or False
# string = 'olá' '7.5' ''

### n1 = input('digite um valor ')
### print(type(n1)) # assim ele vai dizerqual é o tipo de valor que n1 recebe

n1 = int(input('valor 1: '))
n2 = int(input('Valor 2: '))
n3 = n1 + n2
###print('A soma entre ', n1, " e ", n2, " é ", n3)
print('A soma entre {} e {} vale {}'.format(n1, n2, n3))

##### uso dos comando print(n. is...) isalpha, isnumeric, isbolean
##### existem vários is