# 4 jogadores, jogam dados, guarde em um dicionário em ordem crescente e mostre o maior
from random import randint
from time import sleep
from operator import itemgetter
jogada = []
jogo = {}
teste = []
result = dict()
for c in range(0, 4):
    num = randint(1,6)
    jogo[f'jogador {c+1}'] = num
print(jogo)
result = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(jogo)
print(result)
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
print('Ranking dos jogadores: ')
for k, v in enumerate(result):
    print(f'{k+1}: {v[0]} com {v[1]}')
    sleep(1)
