# Informar a hipotenusa de um triangulo a partir de seus catetos
from math import sqrt
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hp = co ** 2 + ca ** 2
h = sqrt(hp)
#h = sqrt(co ** 2 + ca ** 2)
print('A hipotenusa do triangulo de catetos {0} e {1} é {2:.2f}' .format(co, ca, h))

#from math import hypot
#hp = hypot(co, ca)
#print('A hipotenusa do triangulo de cateto {0} e {1} é {2:.2f}'.format(co, ca,hp)
