#Cadastro de pessoas e quantificar a quantidade de adultos, homens e mulheres +20
m = f20 = a = 0
c = ' '
while True:
    i = int(input('Digite a sua idade: '))
    if i >= 18:
        a += 1
    s = ' '
    while s not in 'MF':
        s = str(input('Selecione o seu sexo [M/F]: ')).strip().upper()[0]
    if s == 'M':
        m += 1
    if s == 'F' and i < 20:
        f20 += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        break
print(f'Foram {a} adultos, {m} homens e {f20} mulheres maiores de 20 anos')
