# Função contador() => recebe três parametros e realiza a contagem. 1) 1=>10 2)1=>10 (2) 3)personalizada
from time import sleep
def contagem(a, b, c):
    if a == '':
        a = 0
    if b == '':
        b = 0
    if c == '':
        c = 1
    print(f'Iniciando a contagem de {a} até {b} com cadencia de {c}')
    num = a
    if c == 0:
        c = 1
    if c < 0:
        c = c * -1
    while True:
        print(num, end=' ')
        sleep(0.5)
        if num == b:
            break
        if a < b:
            num += c
            if num > b:
                break
        else:
            num -= c
            if num < b:
                break
    print()


# Código Principal
contagem(1, 10, 1)
contagem(10, 0, 2)
i = (input('Digite um valor para o ínicio da contagem: '))
f = (input('Digite um valor para o fim da contagem: '))
c = (input('Digite um valor para a cadencia da contagem: '))
contagem(i, f, c)
