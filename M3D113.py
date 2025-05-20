# Parecido com o D104, função leiaint() e leiafloat() + tratamento de erro:
def leiaint(txt):
    while True:
        try:
            n = int(input(f'{txt}: '))
        except ValueError:
            print(f'\033[31mERRO! Adicione um valor válido\033[m')
        except KeyboardInterrupt:
            print()
            print(f'\033[31mERRO! O usuário preferiu não adicionar um valor\033[m')
            return 0
        else:
            return n


def leiafloat(txt):
    while True:
        try:
            n = str(input(f'{txt}: ')).strip().replace(',', '.')
            if not n.isalpha():
                n = float(n)
                break
            else:
                print('\033[31mERRO! Digite um valor válido\033[m')
        except ValueError:
            print('\033[31mERRO! Digite um valor válido\033[m')
        except KeyboardInterrupt:
            n = 0
            print()
            print('\033[31mO usuário preferiu não adicionar valor\033[m')
            break
    return n
