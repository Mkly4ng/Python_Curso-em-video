# Lista de alunos, mostra boletim e opcoes de ver a nota individualmente dos alunos
alunos = list()
aluno = list()
notas = list()
count = 0
while True:
    aluno.clear()
    notas.clear()
    aluno.append(str(input('Digite o nome do aluno: ')).strip())
    notas.append(float(input('Digite a primeira nota: ')))
    notas.append(float(input('Digite a segunda nota: ')))
    aluno.append(notas[:])
    alunos.append(aluno[:])
    while True:
        r = str(input('[N/S] Deseja continuar? ')).strip().upper()
        if r in 'SN':
            break
    if r in 'N':
        break
print(alunos)
print('-' * 24)
print(f'{'Número':<8}{'Nome':<10}{'Média':<5}')
for c, a in alunos:
    print(f'{count:<8}{c:<10}{(a[0] + a[1]) / 2:<6}')
    count += 1
while True:
    while True:
        r = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
        if r < len(alunos):
            print(f'As notas de {alunos[r][0]} sao {alunos[r][1]}')
            break
        elif r == 999:
            break
    if r == 999:
        break
