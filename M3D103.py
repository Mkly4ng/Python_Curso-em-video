# Funcao ficha(), recebe dois parametros opcionais, nome e quantidade de gols
def ficha(n='<desconhecido>', g='0'):
    if len(n) <= 0:
        n = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    print(f'O jogador {n} fez {g} gol(s)')


# Código Principal
nome = str(input('Digite o nome do jogador: ')).strip()
gols = str(input('Digite a quantidade de gols: '))
ficha(nome, gols)
