nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
if media >= 6:
    print('Sua média foi de {} e você aprovou' .format(media))
else:
    print('Sua média foi de {} e você reprovou' .format(media))

