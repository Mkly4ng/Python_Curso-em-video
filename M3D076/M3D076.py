#Crie uma tupla com produtos e seus respectivos preços, tabule-os
lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.00,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livros', 34.90)
print('-' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-' * 40)
for c in range(0,len(lista), 2):
    print(f'{lista[c]:.<31}R$ {lista[c+1]:>6.2f}')
print('-' * 40)
#Falta adicionar os pontos entre o nome e os preços
