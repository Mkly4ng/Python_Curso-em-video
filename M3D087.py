#Ampliacao do exercício 86, mostando a soma dos pares, soma da terceira coluna e o maior valor da segunda linh
pares = 0
tc = 0
maior = menor = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para ({l+1},{c+1}): '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0: # Soma dos valores pares
            pares += matriz[l][c]
        if c == 2:
            tc += matriz[l][c]
        if l == 1:
            if c == 0: # Adicionar valor para menor e maior na primeira tentativa
                maior = menor = matriz[l][c]
            else:
                if maior < matriz[l][c]: # Comparar se o valor atual é o maior
                    maior = matriz[l][c]
                if menor > matriz[l][c]: # Comparar se o valora atual é o menor
                    menor = matriz[l][c]
    print()
print(f'A soma dos valores pares é {pares}'
      f'\nA soma dos valores da terceira coluna é {tc}'
      f'\nO maior valor da segunda linha é {maior}'
      f'\nO menor valor da segunda linha é {menor}')
