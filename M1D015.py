# Valor do aluguel de um carro baseado no tempo e kilometragem
d = int(input('Informe a quantidade de dias que o carro foi alugado: '))
km = float(input('Informe a quantidade de kilometros rodados: '))
d1 = d*60
km1 = km*0.15
t = km1 + d1
#t = (d * 60) + (km * 0.15)
print('O total a ser pago é R${0:.2f}'.format(t))
