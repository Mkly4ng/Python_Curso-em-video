#Calculadora de fatoria
n = int(input('Digite o número para calcular sua fatorial: '))
total = 1
cal = 0
m = n
print('{0}! = ' .format(n), end='')
while n != 0:
    print('{0}' .format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    total = total * n # pode ser tbm total total *= n
    n -= 1
print('{1}' .format(m, total))

# usando bibliotecas
# from math import factorial
# f = factorial(n)
