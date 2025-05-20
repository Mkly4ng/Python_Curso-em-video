# Leia o nome e a mádia de um aluno e mostre tudo num dicionário
""""nome = str(input('Nome: ')).strip()
media = float(input(f'Média de {nome}: '))
info = {'nome': nome, 'media': media}"""
info = {}
info['nome'] = str(input('Digite o nome: ')).strip()
info['media'] = float(input(f'Digite a média de {info['nome']}: '))
if info['media'] < 5:
    info['situação'] = 'Reprovado'
elif 5 < info['media'] < 7:
    info['situação'] = 'Recuperaçao'
else:
    info['situação'] = 'Aprovado'
print(info.items())
for k, v in info.items():
    print(f'{k} é igual a {v}')
