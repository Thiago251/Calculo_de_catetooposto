import math
cp = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = math.hypot(cp, ca)
print('O valor do Hipotenusa: {:.2f}'.format(h))