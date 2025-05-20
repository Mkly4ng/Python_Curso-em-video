# Dizer se o numero é primo ou nao
count = 0
n = int(input('Digite o numero que deseja saber se é primo: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m{0}\033[m'.format(c), end=' ')
        count += 1
    elif n % c != 0:
        print('\033[33m{0}\033[m'.format(c), end=' ')
if count == 2:
    print('\n\033[32mO número {0} é primo!\033[m'
          '\nPois ele só é divísivel por {1} números' .format(n, count))
else:
    print('\n\033[31mO número {0} nao é primo\033[m'
          '\nPois ele é divisil por {1} números' .format(n, count))
