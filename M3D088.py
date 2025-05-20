# Mega Sena, perguntr quantos palpites, sortear 6 números entre 1-60 e adicionar cada jogo num lista composta
from random import randint
from time import sleep
print(f'-' * 31)
print(f'{'JOGA NA MEGA SENA':^31}')
print(f'-' * 31)
quant = int(input('Quantos palpites voce deseja? '))
palpites = []
num = []
for vezes in range(0, quant):
    for c in range(0, 6):
        n = randint(1, 60)
        while True:
            if n not in num:
                num.append(n)
                break
            else:
                n = randint(1, 60)
    palpites.append(num[:])
    num.clear()
for r in range(0, len(palpites)):
    sleep(1)
    palpites[r].sort()
    print(f'Jogo {r+1}: {palpites[r]}')
print(f'-' * 8, '< BOA SORTE! >', '-' * 8)
