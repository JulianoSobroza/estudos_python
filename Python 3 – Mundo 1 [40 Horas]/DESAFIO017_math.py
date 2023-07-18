import math
c1 = float(input('Comprimento do CO: '))
c2 = float(input('Comprimento do CA: '))
h = math.hypot(c1, c2)
print('A hipotenusa mede: {:.3f}'.format(h))