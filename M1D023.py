# separar um número de 4 digitos em milhar, centena, dezena e unidade
'''num = int(input('Digite um número entre 0000 e 9999: '))
n = str(num)
print('unidade: {0}
dezena: {1}
centena: {2}
milhar: {3}' .format(n[3], n[2], n[1], n[0]))'''

v = int(input('Digite um número entre 0000 e 9999: '))
u = v // 1 % 10
d = v // 10 % 10
c = v // 100 % 10
m = v // 1000 % 10
print('''unidade: {0}
dezena: {1}
centena: {2}
milhar: {3}''' .format(u, d, c, m))
