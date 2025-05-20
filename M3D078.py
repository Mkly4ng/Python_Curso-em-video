# 5 valores na lista, mostrar o maior e o menor e suas respectivas posiçoes
lista = []
maior = 0
menor = 0
for n in range(0, 5):
    lista.append(int(input(f'Digite um número para a posiçao {n + 1}: ')))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] >= maior:
            maior = lista[n]
        if lista[n] <= menor:
            menor = lista[n]
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {maior}', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}. . .', end='')
print()
print(f'O menopr valor foi {menor} nas posicoes', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}. . .', end='')

