# Desafio 107, módulo moeda.py funções aumentar(), diminuir(), dobro() e metade() // __init__.py
def aumentar(n, a):
    aum = n * (1 + (a / 100))
    return aum


def reduzir(n, d):
    dim = n * (1 - (d / 100))
    return dim


def dobro(n):
    dob = n * 2
    return dob


def metade(n):
    met = n / 2
    return met


def moeda(n):
    moe = (f'R${n:.2f}')
    return moe
