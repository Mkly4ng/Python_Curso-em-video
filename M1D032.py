# Descobrir se é um ano bissexto
from datetime import date  # serve para pegar a data da máquina
a = int(input('Digite o ano que quer analisar ou coloque 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('o ano {0} é bissexto' .format(a))
else:
    print('o ano {0} nao é bissexto' .format(a))
