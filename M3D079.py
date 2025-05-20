# Adicionar quantos números quiser a uma lista, nao adicionar repetidos e mostrar em ordem crescente
lista = []
while True:
    num = int(input('Digite um número a ser adicionado: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, tente novamente')
    while True:
        resposta = str(input('[S/N] Deseja continuar? ')).upper().strip()
        if resposta in 'SN':
            break
    if resposta in 'N':
        break
lista.sort()
print(lista)
