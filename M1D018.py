# Informar o seno, cosseno e tangente de um angulo em radianos
from math import sin, cos, tan, radians
a = float(input('Digite o valor do angulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
#print(' Seno de {0} é {1}\n Cosseno de {0} é {2}\n Tangente de {0} é {3}' .format(a, s, c, t))
print('''O seno de {0} é {1:.2f}
O cosseno de {0} é {2:.2f}
A tangente de {0} é {3:.2f}''' .format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))
