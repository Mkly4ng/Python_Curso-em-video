#Jogo de Jokenpo
from time import sleep
from random import choice
print('=' * 20)
print('Vamos jogar Jokenpo?')
print('=' * 20)
sleep(0.5)
j = str(input('Escolha entre pedra, papel e tesoura: ')).lower().strip()
if j == 'pedra' or j == 'papel' or j == 'tesoura':
    sleep(0.5)
    print('\033[37mPensando. . .\033[m')
    sleep(0.5)
    print('Jo')
    sleep(0.5)
    print('Ken')
    sleep(0.5)
    print('Po')
    sleep(0.5)
pc = ['pedra', 'papel', 'tesoura']
p = choice(pc)
if p == pc[0] and j == 'pedra':
    print(p)
    print('\033[33mEmpatamos')
elif p == pc[0] and j == 'papel':
    print(p)
    print('\033[32mVocê ganhou')
elif p == pc[0] and j == 'tesoura':
    print(p)
    print('\033[31mVocê perdeu')
elif p == pc[1] and j == 'pedra':
    print(p)
    print('\033[31mVocê perdeu')
elif p == pc[1] and j == 'papel':
    print(p)
    print('\033[33mEmpatamos')
elif p == pc[1] and j == 'tesoura':
    print(p)
    print('\033[32mVocê ganhou')
elif p == pc[2] and j == 'pedra':
    print(p)
    print('\033[32mVocê ganhou')
elif p == pc[2] and j == 'papel':
    print(p)
    print('\033[31mVocê perdeu')
elif p == pc[2] and j == 'tesoura':
    print(p)
    print('\033[33mEmpatamos')
else:
    print('''\033[31mEra pra escolher entre pedra, papel e tesoura.''')
