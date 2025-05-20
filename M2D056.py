#Receba nome e idade de diferentes pessoas e retorna a idade média do grupo, quem é e quantos anos tem o mais velho e a quantidade de mulheres menores de 20 anos
nome = ''
im = 0
t = 0
count = 0
for l in range(1, 5):
    print('===== {0} {1} ====='.format(l, 'pessoa'))
    n = input('Nome: ').lower().strip()
    i = int(input('Idade: '))
    s = str(input('[M/F]: ')).lower().strip()
    t += i
    if s == 'm' and l == 1:
        nome = n
        im = i
    elif s == 'm' and l != 1:
        if i > im:
            im = i
            nome = n
    if s == 'f' and i < 20:
        count += 1
print('A média de idade do grupo é de {0} anos'.format(t / 4))
print('O homem mais velho tem {0} anos e se chama {1}'.format(im, nome.capitalize()))
print('Ao todo sao {0} mulheres com menos de 20 anos'.format(count))
