#D051 2.0 => P.A.
p1 = float(input('Digite o primeiro termo da P.A.: '))
r = float(input('Digite a razao da P.A.: '))
count = 0
pa = []
while count < 10:
    pa.append(p1 + (r * count))
    count += 1
print('Os 10 primeiros termos da P.A. sao {0}' .format(pa))
count = 0
# Gabarito
while count < 10:
    print('{0} => ' .format(p1), end= '')
    p1 += r
    count += 1
print('Fim')
