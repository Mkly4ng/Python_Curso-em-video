#Funçao que mostre o fatorial e opçao de mostrar ou nao o calculo. help(fatoral) deve mostrar como usar a ferramenta
def fatorial(n, show='N'):
    '''
    => Calcula o Fatorial de um número.
    :param n: o número a ser calculado
    :param show: (opicional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    '''
    r = 1
    cal = []
    while n != 0:
        cal.append(n)
        r *= n
        n -= 1
    print('Resultado:')
    print(r)
    if show == 'S':
        print('Calculo:')
        for n in cal:
            print(n, end=' ')
            if n != cal[-1]:
                (print('x', end=' '))
        print(f'= {r}')


# Código Principal
n = int(input('Digite o número a ter a fatorial calculada: '))
while True:
    show = str(input(f'[S/N] Se deseja ver o calculo de {n}! ')).strip().upper()
    if show in 'SN':
        break
    else:
        print('\033[31mERRO! Digite S/N\033[m')
fatorial(n, show)
help(fatorial)
