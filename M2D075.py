#Recebe 4 números pelo console, mostre-os, indique quantos 9, posicao do primeiro 3 e quais sao pares
lista = []
count = 0
for c in range(0, 4):
    n1 = int(input('Digite um número: '))
    lista.append(n1)
list = lista[0], lista[1], lista[2], lista[3]
quant9 = list.count(9)
#for c in range(-1, 3):
#    if lista[c] % 2 == 0:
#        count += 1
print(f'Voce digitou os números {list}')
if quant9 == -1:
    print('O valor 9 nao apareceu')
else:
    print(f'O valor 9 apareceu {quant9} vezes')
if 3 in lista:
    loc3 = lista.index(3)
    print(f'O valor 3 apareceu pela primeira vez na {loc3 + 1} posicao')
else:
    print('O valor 3 nao apareceu')
#print(f'Foram {count} valores pares digitados')
print('Os valores pares digitados foram:', end=' ')
for c in lista:
    if c % 2 == 0:
        print(c, end=' ')
