# jogo, adivinhar um numero entre 0 e 5
from time import sleep
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('''  Vamos jogar? Eu pensei em um número entre 0 a 5''')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
sleep(1)
from random import choice
lista = [0, 1, 2, 3, 4, 5]
n = int(input('Qual número voce acha que é? ')) # resposta do jogador
m = choice(lista)
print('Processando...')
sleep(2)
if m == n:
    print('Parabéns!!! Voce ganhou!!!')
else:
    print('Ganhei!!! Era o número {0} e não o {1}' .format(m, n))

# from random import radiant
# n = radiant(0, 5)
