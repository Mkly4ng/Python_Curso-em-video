#Crie uma matriz 3x3 (9 itens) usando uma lista
matriz = [[[], [], []], [[], [], []], [[], [], []]]
for c in range(0, 9):
    if c < 3:
        n = int(input(f'Digite o termo [/]: '))
        matriz[0][c].append(n)
    elif c > 5:
        n = int(input(f'Digite o termo [/]: '))
        matriz[2][c - 6].append(n)
    else:
        n = int(input(f'Digite o termo [/]: '))
        matriz[1][c - 3].append(n)
    print(c)
for c in range(0, 3):
    print(f'{matriz[c]}')
