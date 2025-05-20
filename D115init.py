# Função leiadinheiro() para checar se o valor é monetário ou não
def leiadinheiro(txt):
    while True:
        n = str(input(f'{txt}')).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print(f'\033[31mErro! {n} não é um valor de preço!\033[m')
        else:
            n = float(n)
            return n


def cor(n=''):
    cor = f'\033[{n}m'
    return cor


def linha():
    print('~' * 40)


def titulo(txt, cor=''):
    """
    => Função para colocar titulos coloridos
    :param txt: Texto do título
    :param cor: Código da cor no padrão ANSI (só o número)
    :return: NADA
    """
    linha()
    print(f'\033[{cor}m'f'{txt:^40}\033[m')
    linha()

def leiaint(txt):
    while True:
        try:
            n = int(input(f'{txt} '))
        except ValueError:
            print(f'\033[31mERRO! Adicione um valor válido\033[m')
        except KeyboardInterrupt:
            print()
            print(f'\033[31mERRO! O usuário preferiu não adicionar um valor\033[m')
            n = 3
            break
        else:
            break
    return n


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cor(33)}{c}{cor()} - {cor(34)}{item}{cor()}')
        c += 1
    linha()
    resp = leiaint(f'{cor(32)}Sua Opção:{cor()}')
    return resp

