# Com uma funçao e retorno, a pessoa informa a data de nascimento, e informa obrigatoriedade de voto ou nao\
from datetime import datetime
def voto(i):
    if 18 <= (datetime.now().year - i) < 65:
        return 'VOTO OBRIGATÓRiO'
    elif (16 <= (datetime.now().year - i) < 18) or (65 <= (datetime.now().year - i)):
        return 'VOTO OPICIONAL'
    elif (datetime.now().year - i) < 16:
        return 'NÃO VOTA'


i = int(input('Em que ano voce nasceu? '))
r = voto(i)
print(f'Com {(datetime.now().year - i)} anos: {r}')
