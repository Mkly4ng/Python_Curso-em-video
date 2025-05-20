# Funcao leiaInt(), funciona como um input(), mas só aceita números
def leiaint(b):
    while True:
        a = str(input(b))
        if a.isnumeric():
            a = int(a)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
    return a


# Programa Principal:
c = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {c}')
