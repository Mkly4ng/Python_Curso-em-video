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
