#Cadastro de uma pessoa, nome, ano de nascimento, carteira de trabalho num dicionário
#Caso tenha carteira, cadastre ano de contratacao, salario e mostre em quantos anos essa pessoa irá se aposentar
from datetime import datetime
cad = dict()
cad['nome'] = str(input('Nome: ')).strip()
cad['idade'] = datetime.now().year - (int(input('Ano de Nascimento: ')))
cad['ctps'] = int(input('Carteira de Trabalho (0 = não tem): '))
if cad['ctps'] != 0:
    cad['contratação'] = int(input('Ano de contratação: '))
    cad['salário'] = int(input('Valor do salário: R$ '))
    cad['aposentadoria'] = cad['idade'] + (35 - (datetime.now().year - cad['contratação']))
for k, v in cad.items():
    print(f' - {k} tem o valor {v}')
