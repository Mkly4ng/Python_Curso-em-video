#Cadastrar diferentes pessoas, mostrar a quantidade do grupo, a média das idades, as mulheres cadastradas e a lista de pessoas que estao a cima da média
grupo = []
pessoa = {}
media = 0
mulheres = []
media2 = []
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('[M/F] Sexo: ')).upper().strip()[0] #[0] == fateamento para pegar só a primeira letra
        if pessoa['sexo'] in 'MF':
             break
        print('ERRO! So é considerado M/F')
    pessoa['idade'] = int(input('idade: '))
    media += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        resp = str(input('[S/N] Deseja continuar? ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! só é valido S/N')
    if resp == 'N':
        break
for c in range(0, len(grupo)):
    if grupo[c]['sexo'] == 'F':
        mulheres.append(grupo[c]['nome'])
    if grupo[c]['idade'] >= (media / len(grupo)):
        media2.append(grupo[c].copy())
print('-=' * 30)
print(f'- O grupo tem {len(grupo)} pessoas.'
      f'\n- A média de idade é de {media / len(grupo)} anos.'
      f'\n- As mulheres do grupo foram {mulheres}'
      f'\n- Lista de pessoas que estao acima da média:')
for c in range(0, len(media2)):
    print()
    for k, v in media2[c].items():
        print(f'{k} = {v};', end=' ')
print()
print('<<FINALIZADO>>')
