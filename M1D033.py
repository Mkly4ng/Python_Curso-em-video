# Descobrir qual é o maior e menor número da lista
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
# Verificar quem é o menor número:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificar o maior número:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {0}\nO menor número é {1}' .format(maior, menor))
