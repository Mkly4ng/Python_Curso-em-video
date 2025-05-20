# Le P1 e R e calcula a Pa dos 10 primeiros números
P1 = float(input('Digite o primeiro termo da sua P.A.: '))
R = float(input('Digite o valor da razao da P.A.: '))
for c in range(0,10):
    print('{0}' .format(c * R + P1), end=' => ')
print('Acabou')
