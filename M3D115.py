# Lista que cadastra e armazena nomes
from D115 import dado
from time import sleep
from D115 import arquivo

arq = 'lista.txt'
if arquivo.arqExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    arquivo.criarArquivo(arq)

while True:
    sleep(0.5)
    resp = dado.menu(['Ver lista', 'Cadastrar pessoa', 'Sair'])
    sleep(0.5)
    if resp == 1:
        arquivo.lerArquivo(arq)
    elif resp == 2:
        dado.titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = dado.leiaint('Idade:')
        arquivo.cadastrar(arq, nome, idade)
        nome = idade = ''
    elif resp == 3:
        dado.titulo('SAINDO, ATÉ LOGO!')
        break
    else:
        print(f'{dado.cor(31)}ERRO: Por favor, digite um número inteiro válido{dado.cor()}')
