# A soma de todos os números ímpares entre 0 e 500 que sejam multiplos de 3
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s += c
print('A soma de todos os números ímpares entre 0 a  500 que sejam múltiplos de 3 é {0}\nForam {1} números' .format(s, cont))
