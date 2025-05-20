#Lista com o nome de váias pessoas, quants pessoas cadastradas, lista com as mais pesadas e a lista com as mais leves
pessoas = list()
pessoa = list()
pp = list()
pl = list()
maior = list()
menor = list()
while True:
    pessoa.append(str(input('Digite o nome: ').strip()))
    pessoa.append(float(input('Digite o peso [kg]: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    while True:
        resposta = str(input('[S/N] Deseja continua? ')).strip().upper()
        if resposta in 'SN':
            break
    if resposta in 'N':
        break
for p in range(0, len(pessoas)):
    if pessoas[p][1] >= 100:
        pp.append(pessoas[p][0])
    else:
        pl.append(pessoas[p][0])
print(f'Foram adicionadas {len(pessoas)}'
      f'\nAs pessoas mais pesadas: {pp}'
      f'\nAs pessoas mais leves: {pl}')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in pessoas:# faz a leitura de cada peso e compara com o maior, caso seja igual escreve o nome cujo o peso pertence
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in pessoas:# faz a leitura de cada peso e compara com o menor, caso seja igual escreve o nome cujo o peso pertence
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
