# Comparar qual número é maior
n1 = float(input('Digite o primeiro valor a ser comparado: '))
n2 = float(input('Digite o segundo valor a ser comparado: '))
if n1 > n2:
    print('{0} é maior que {1}'.format(n1, n2))
elif n2 > n1:
    print('{0} é maior que {1}'.format(n2, n1))
elif n1 == n2:
    print('Os dois números possuem o mesmo valor')
