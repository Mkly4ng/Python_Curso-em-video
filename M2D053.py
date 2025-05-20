# Checar se a frase é um palíndromo
f = str(input('Digite a frase desejada: ')).lower().strip().replace(' ', '')
n = len(f)
count = n
t = []
for c in range(0, n, ):
    t.append(f[count - 1: count])
    count += -1
# print(''.join(t))
e = (2 * n + 5)
print('=' * e)
print(' {0}'.format('{0} {1} {2}'.format(f, '&', ''.join(t))))
print('=' * e)
if f == ''.join(t):
    print('\033[32mA palavra {0} é um palindromo\033[m'.format(f))
else:
    print('\033[31mA palavra{0} nao é um palindromo\033[m'.format(f))
