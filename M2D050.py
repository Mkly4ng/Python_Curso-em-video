# soma de todos os números pares, ímpares sao desconsiderados
s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} número: ' .format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma final dos {1} números pares é {0}' .format(s, cont))
