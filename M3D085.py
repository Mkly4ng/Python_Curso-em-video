#Adicionar 7 número a uma lista, essa lista adeve ter duas sublistas, uma com pares e outra com ímpares
lista = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1} número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print('-=-'* 20)
print(f'Os valores pares digitados foram: {lista[0]}'
      f'\nOS valores ímpares digitados foram: {lista[1]}')
