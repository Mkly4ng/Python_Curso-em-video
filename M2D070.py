# lista de compras com total gasto, quantos produtos custam mais de 1000 e o mais barato
total = quant = v1 = 0
menor = ''
while True:
    p = str(input('Digite o nome do produto: ')).strip().lower()
    v = float(input('Digite o valor do produto: R$ '))
    total += v
    if v > 1000:
        quant += 1
    if v1 == 0 or v1 >= v:
        v1 = v
        menor = p
    #if v1 >= v:
    #    v1 = v
    #    menor = p
    c = ' '
    while c not in 'sn':
        c = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if c == 'n':
        break
print(f'O valor total foi de R${total}'
      f'\nForam {quant} produtos a cima de R$1000.00'
      f'\nO produto mais barato foi {menor}')
