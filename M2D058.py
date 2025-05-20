# D028 2.0 advinhe um número entre 0 a 10
from random import choice
from time import sleep
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Vamos jogar um jogo?')
sleep(0.5)
print('Estou pensando em um número entre 0 a 10, tente adivinha-lo!')
pc = choice(lista)
count = 0
j = ''
while j != pc:
    j = int(input('Qual número estou pensando? '))
    count += 1
    if j > pc:
        print('Menos... Tente de novo')
    elif j < pc:
        print('Mais... Tente de novo')
print('Voce acertou, eu estava pensando no número {1}, foram {0} tentativas!' .format(count, pc))

# Opçao alternativa para o while
# acertou = False
# while not acertou:
# if j == computador
#   acertou = True
