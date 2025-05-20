#Gere 5 números e adicione a tupla, mostre o menor e o maior deles
from random import choice
lista = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
list = []
maior = 0
menor = 0
for c in range(0, 5):
    n1 = int(choice(lista))
    if c == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    list.append(n1)
print(f'Os números foram {list}'
      f'\nO maior número é {maior}'
      f'\nO menor número é {menor}')
