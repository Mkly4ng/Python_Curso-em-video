#lista chamada números e duas funções => sorteia() e somaPar() sorteio de 5 números numa lista a segunda vai somar os pares sortiados
from random import randint
from time import sleep
lista = list()
def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        b = randint(0,10)
        lista.append(b)
        print(b, end=' ')
        sleep(0.5)
    print()


def somaPar():
    sorteia()
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}')


somaPar()
