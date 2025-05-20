# Função maior() => recebe vários parametros inteiros e verifica qual é o maior em cada
from time import sleep
def maior(*num):
    maior = count = 0
    print('-=' * 30)
    print('Analisando os valores informados. . .')
    for c in num:
        print(c, end=' ', flush=True)
        count += 1
        sleep(0.5)
        if count == 0:
            maior = c
        else:
            if c > maior:
                maior = c
    print(f'Foram informados {count} valores')
    print(f'O maior valor informado foi {maior}')
maior(6, 5, 4, 3, 2, 1)
