# Seleçao de Sexo
c = ''
while c != 1:
    s = str(input('Digite o seu sexo, [M/F]: ')).strip().lower()[0] #pegar só a primeira letra
    if s == 'm' or s == 'f':
        c = 1
    else:
        print('\033[31mOpçao incorreta!\033[m')
if s == 'm':
    print('Sexo reconhecido, masculino')
elif s == 'f':
    print('Sexo reconhecido, feminino')
