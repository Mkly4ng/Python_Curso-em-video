#Atualizaçao do D093, mais jogadores e painel interativo
jog = dict()
gols = list()
total = 0
lista = []
while True:
    jog['Nome'] = str(input('Nome do jogador: ')).strip()
    quant = int(input(f'Quantas partidas {jog['Nome']} jogou? '))
    for c in range(0, quant):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jog['gols'] = gols[:]
    for gol in gols:
        total += gol
    jog['total'] = total
    total = 0
    gols = []
    lista.append(jog.copy())
    while True:
        resp = str(input('[S/N] Deseja continuar? ')).strip().upper()
        if resp in 'SN':
            break
    if resp in 'N':
        break
print(f'-' * 40)
print(f'{'cod':<4}{'Nome':<15}{'gols':<15}{'total':<5}')
print(f'-' * 40)
for c in range(0, len(lista)):
    print(f'{c:<4}{lista[c]['Nome']:<15}{lista[c]['gols']}{lista[c]['total']:>5}')
print(f'-' * 40)
while True:
    resp = (int(input('Mostrar dados de qual jogador? [999 para sair] ')))
    print(f'-' * 40)
    if resp == 999:
        print('<< VOLTE SEMPRE >>')
        break
    elif resp > len(lista) - 1:
        print(f'\033[31mERRO!\033[m Não existe jogador com o código {resp}! Tente novamente!')
    else:
        print(f'Levantamento do jogador {lista[resp]['Nome']}')
        for k in range(0, len(lista[resp]['gols'])):
            print(f'No jogo {k+1} fez {lista[resp]['gols'][k]}')
