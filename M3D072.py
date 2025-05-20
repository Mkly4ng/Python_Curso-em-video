#Uma tupla de 0-20, quando escolhido um número, ele é digitado por extenso
lista = ('zero', 'um', 'dois', 'tres', 'quatro',
         'cinco', 'seis', 'sete', 'oito',
         'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um valor entre 0 a 20: '))
        if 0 <= n <= 20:
         break
        print('Tente novamente!')
    print(f'{lista[n]} foi o número escolhido')
    r = ''
    r = str(input('Voce deseja continuar? [S/N]: ')).lower().strip()
    if r == 'n':
        break
