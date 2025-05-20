# Ver se 7 pessoas sao maiores ou menores de 21 anos
from datetime import date
lista = []
a = 0
c = 0
for d in range(0, 7):
    n = int(input('Digite o ano de nascimento: '))
    lista.append(n)
for d in range(0, 7):
    if date.today().year - lista[d] < 21:
        c += +1
    elif date.today().year - lista[d] >= 21:
        a += +1
print('Tiveram {0} maiores de idade e {1} menores de idade' .format(a, c))
