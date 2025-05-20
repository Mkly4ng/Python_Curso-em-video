#Par ou ímpar com o computador, só para quando o jogador perder
from random import choice
from time import sleep
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
while True:
    print('=' * 30)
    print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^30}')
    print('=' * 30)
    n = int(input('Digite um valor: '))
    e = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    pc = choice(lista)
    if (n + pc) % 2 == 0:
        print(f'Voce jogou {n} e o computador {pc}, deu Par!')
    else:
        print(f'Voce jogou {n} e o computador {pc}, deu Ímpar!')
    if e == 'P':
        if (n + pc) % 2 == 0:
            count += 1
            sleep(1)
            print('\033[32mVoce venceu!\033[m')
        else:
            break
    if e == 'I':
        if (n + pc) % 2 != 0:
            count += 1
            sleep(1)
            print('\033[32mVoce venceu!\033[m')
        else:
            break
sleep(1)
print(f'\033[31mGAME OVER!\033[m Voce ganhou {count} vezes!')
