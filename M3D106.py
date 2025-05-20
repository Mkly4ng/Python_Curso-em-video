# Faça uma Funçao que use o PyHELP (obs:use cores)
from time import sleep
def titulo(txt, cor=''):
    """
    => Função para colocar titulos coloridos
    :param txt: Texto do título
    :param cor: Código da cor no padrão ANSI (só o número)
    :return: NADA
    """
    print(f'\033[{cor}m''~' * (len(txt) + 4))
    print(f'\033[{cor}m'f'  {txt}')
    print(f'\033[{cor}m''~' * (len(txt) + 4))
def pyhelp():
    """
    => Função para rodar o help() com cores pelo console
        Obs: use "fim" para encerrar
    :return: NADA
    """
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', 42)
        sleep(0.7)
        fun = str(input('\033[mFunção ou Biblioteca > ')).lower().strip()
        if fun == 'fim':
            titulo('ATÉ LOGO!', 41)
            break
        sleep(0.5)
        titulo(f'Acessando o maunal do comando "{fun}"', 44)
        sleep(0.4)
        print(f'\033[7m')
        help(fun)
        print(f'\033[m')
        sleep(0.4)


pyhelp()
