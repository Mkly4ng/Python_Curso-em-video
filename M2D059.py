#Calculadora
print('Bem vindo a calculadora!')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
c = 0
while c != 7:
    print('{0} {1} {2}' .format('=' * 10, 'OPÇOES', '=' * 10))
    print('[1] somar'
          '\n[2] subtrair'
          '\n[3] multiplicar'
          '\n[4] dividir'
          '\n[5] maior'
          '\n[6] novos números'
          '\n[7] sair do programa')
    print('=' * 28)
    c = int(input('Qual opçao deseja? '))
    if c == 1:
        print('\033[32mResultado: {}\033[m' .format(n1 + n2))
    elif c == 2:
        print('\033[32mResultado: {}\033[m' .format(n1 - n2))
    elif c == 3:
        print('\033[32mResultado: {}\033[m' .format(n1 * n2))
    elif c == 4:
        print('\033[32mResultado: {}\033[m' .format(n1 / n2))
    elif c == 5:
        if n1 > n2:
            print('\033[32m{0} é o maior valor\033[m' .format(n1))
        else:
            print('\033[32m{0} é o maior valor\033[m' .format(n2))
    elif c == 6:
        n1 = int(input('\033[32mDigite o primeiro novo valor: \033[m'))
        n2 = int(input('\033[32mDigite o segundo novo valor: \033[m'))
        print('{0} {1}' .format(n1, n2))
    elif c == 7:
        ''
    else:
        print('\033[31mOpçao nao disponível\033[m')
print('\033[32mObrigado por usar a calculadora! =D\033[m')
