#Adicione 6 pesos a uma lista e indique qual é o maior e qual é o menor
lista = []
for c in range(1, 6):
    p = float(input('Digite o {0} peso: ' .format(c)))
    lista.append(p)
n1 = lista[0]
n2 = lista[1]
n3 = lista[2]
n4 = lista[3]
n5 = lista[4]
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print('{} é o maior número' .format(n1))
elif n2 > n3 and n2 > n4 and n2 > n5:
    print('{} é o maior número' .format(n2))
elif n3 > n4 and n3 > n5:
    print('{} é o maior número' .format(n3))
elif n4 > n5:
    print('{} é o maior número' .format(n4))
else:
    print('{} é o maior número' .format(n5))
if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
    print('{} é o menor número' .format(n1))
elif n2 < n3 and n2 < n4 and n2 < n5:
    print('{} é o menor número' .format(n2))
elif n3 < n4 and n3 < n5:
    print('{} é o menor número' .format(n3))
elif n4 < n5:
    print('{} é o menor número' .format(n4))
else:
    print('{} é o menor número' .format(n5))
