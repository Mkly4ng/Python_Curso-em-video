# radar com limite de 80 km/h
v = int(input('Qual é a velociadade do carro? '))
if v > 80:
    print('MULTADO! Ultrapassou o limite de 80km/h, a multa é de R${0}' .format((v-80)*7))

