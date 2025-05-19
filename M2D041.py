# Informa a categoria a partir da idade
# i = int(input('Digite a sua idade para saber a sua categoria: '))
from datetime import date
a = int(input('informe o ano de nascimento: '))
i = date.today().year - a
if i >= 0:
    print('idade: {0} anos' .format(i))
# correçao das faixas etárias
'''if 0 <= i < 9:
    print('Categoria: Mirim')
elif 8 < i < 14:
    print('Categoria: Infantil')
elif 13 < i < 19:
    print('Categoria: Junior')
elif 18 < i < 20:
    print('Categoria: Senior')
elif i >= 20:
    print('Categoria: Master')
else:
    print('\033[31mIdade digitada errada')'''
if 0 <= i <= 9:
    print('Categoria: Mirim')
elif 9 < i <= 14:
    print('Categoria: Infantil')
elif 14 < i <= 19:
    print('Categoria: Junior')
elif 19 < i <= 25:
    print('Categoria: Senior')
elif i > 25:
    print('Categoria: Master')
else:
    print('\033[31mIdade digitada errada')
