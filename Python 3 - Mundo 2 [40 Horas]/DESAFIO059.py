"""
Exercício Python 059: Crie um programa que leia dois valores e mostre 
um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = (int(input('>>>>>>Qual operação vc deseja realizar? ')))
    if opção == 1:
        print(n1 + n2)
    elif opção == 2:
        print(n1 * n2 )
    elif opção == 3:
        if n1 > n2:
            print('{} é maior'.format(n1))
        elif n1 < n2:
            print('{} é maior.'. format(n2))
    elif opção == 4:
        print('Informe os números novamente.')
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')   
print('Fim do programa.')



