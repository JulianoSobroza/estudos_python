"""
O comando while faz com que um conjunto de instruções seja executado enquanto 
 uma condição é atendida. Quando o resultado dessa condição passa a ser falso,
   a execução do loop é interrompida, como mostra o exemplo a seguir:
"""

"""
# exemplo, vai contar de 0 até 4 e vai parar

contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
      print("O loop while foi encerrado com sucesso!")
"""

"""
#exemple 2:
# program to calculate the sum of numbers
# until the user enters zero

total = 0

number = int(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number    # total = total + number
    
    # take integer input again
    number = int(input('Enter a number: '))
    

print('total =', total)
"""

# infinite loop
age = 32

# the test condition is always True
while age > 18:
    print('You can vote')