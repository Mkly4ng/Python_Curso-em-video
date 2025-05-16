# Valor da viagem conforme a kilometragem
km = int(input('Digite a distancia em km: '))
if km <= 200:
    print('O valor é de R${0:.2f}' .format(km*0.5))
else:
    print('O valor é de {0:.2f}' .format(km*0.45))
print('O valor é de R${0:.2f}' .format(km*0.5)) if km <= 200 else print('O valor é de {0:.2f}' ,format(km*0.45))
