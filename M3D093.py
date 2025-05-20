#Aproveitamento dos jogos de um jogador de futebol
jog = dict()
gols = list()
total = 0
jog['Nome'] = str(input('Nome do jogador: ')).strip()
quant = int(input('Quantas partidas ele jogou? '))
for c in range(0, quant):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
jog['gols'] = gols[:]
#total = sum(gols) mesma coisa das linhas 11/12
for gol in gols:
    total += gol
jog['total'] = total
print('-=' * 30)
print(jog)
print('-=' * 30)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jog['Nome']} jogou {quant} partidas')
for c in range(0, quant):
    print(f'    => Na partida {c + 1}, fez {gols[c]} gols')
print(f'Foi um total de {jog['total']} gols')
for i, v in enumerate(jog['gols']): #modo diferente de fazer o que está nas linhas 20/21
    print(f'    => Na partida {i + 1}, fez {v} gols')
print(sum(gols))
