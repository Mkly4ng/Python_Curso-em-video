def aumentar(n, a, m=False):
    aum = n * (1 + (a / 100))
    if m:
        return moeda(aum)
    else:
        return aum


def reduzir(n, d, m=False):
    dim = n * (1 - (d / 100))
    if m:
        return moeda(dim)
    else:
        return dim


def dobro(n, m=False):
    dob = n * 2
    if m:
        return moeda(dob)
    else:
        return dob


def metade(n, m=False):
    met = n / 2
    if m:
        return moeda(met)
    else:
        return met


def moeda(n=0):
    moe = (f'R${n:>.2f}'.replace('.', ','))
    return moe


def resumo(n, a, d):
    print('~' * 30)
    print(f'        {'RESUMO DO VALOR'}')
    print('~' * 30)
    print(f'Preço analisado:    {moeda(n)}')
    print(f'Dobro do preço:     {dobro(n, True)}')
    print(f'Metade do preço:    {metade(n, True)}')
    print(f'{a}% de aumento:     {aumentar(n, a, True)}')
    print(f'{d}% de redução:     {reduzir(n, d, True)}')
    print('~' * 30)


# Função leiadinheiro() para checar se o valor é monetário ou não
def leiadinheiro(txt):
    while True:
        n = str(input(f'{txt}')).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print(f'\033[31mErro! {n} não é um valor de preço!\033[m')
        else:
            n = float(n)
            return n
