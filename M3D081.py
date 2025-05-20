# Lista com vários números, quantos números, a lista de forma decrescente e se o 5 está na lista
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        resposta = str(input('[S/N] Deseja continuar? ')).upper().strip()
        if resposta in 'SN':
            break
    if resposta in 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} numeros'
      f'\n os valores foram {lista}')
if 5 in lista:
    print('O número 5 está presente na lista')
else:
    print('O número 5 nao foi adicionada a lista')
