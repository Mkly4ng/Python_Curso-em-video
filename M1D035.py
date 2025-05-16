# Se é possivel formar um triangulo a partir dos valores
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
# Tentativa antes da aula 11
'''if (r1 + r2) > r3:
    c1 = 0
else:
    c1 = 1
if (r1 + r3) > r2:
    c2 = 0
else:
    c2 = 1
if (r2 + r3) > r1:
    c3 = 0
else:
    c3 = 1
if c1 + c2 + c3 == 0:
    print('As retas {0}, {1} e {2} podem formar um triangulo' .format(r1, r2, r3))
else:
    print('As retas nao podem formar um triangulo')'''
# Pós aula 11
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {0}, {1} e {2} {3}podem formar um triangulo{4}' .format(r1, r2, r3, '\033[32m', '\033[1m'))
else:
    print('As retas {0}, {1}, {2} {3}nao podem formar um triangulo{4}' .format(r1, r2, r3, '\033[31m', '\033[m'))
