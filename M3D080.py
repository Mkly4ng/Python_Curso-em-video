# cinco números em uma lista, ordene-os sem usar o sort()
lista = []
menor = 0
maior = 0
n = 0
for c in range(0, 5):
    num = int(input(f'Digite o {c + 1} valor: '))
    if c == 0:
        lista.insert(0, num)
        menor = num
        maior = num
        n = num
    else:
        if num <= menor:
            lista.insert(0, num)
            menor = num
            print('Foi adicionado no inicio da lista. . .')
        elif num >= maior:
            lista.insert((lista.index(maior)+1), num)
            maior = num
            print('foi adicionado ao final da lista. . .')
        elif maior >= num >= menor:
            if num >= n:
                lista.insert((lista.index(n)+1), num)
            else:
                lista.insert((lista.index(n)), num)
        else:
            lista.insert((lista.index(menor)+1), num)
        n = num
    print(lista) #só confirmar o que tá acontecendo
print(lista)
