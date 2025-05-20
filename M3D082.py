#Varios numeros entram, lista geral, lista de pares, lista de impares
listat = []
listap = []
listai = []
while True:
    num = int(input('Digite um número: '))
    listat.append(num)
    if num % 2 == 0:
        listap.append(num)
    else:
        listai.append(num)
    while True:
        resposta = str(input('[S/N] Deseja continuar? ')).upper().strip()
        if 'S' in resposta or 'N' in resposta:
            break
    if 'N' in resposta:
        break
print(f'Os números digitados foram {listat}'
      f'\nOs pares sao {listap}'
      f'\nOs ímpares sao {listai}')
