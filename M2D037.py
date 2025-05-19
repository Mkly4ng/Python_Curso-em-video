# Transformar um número de decimal para outros formatos
n = int(input('Digite o número que voce quer transformar: '))
b = str(input('Em qual das bases voce quer transformar? Binário, Octal ou Hexadecimal: ')).lower().strip()
if b == 'binário' or b == 'binario':
    print('O valor {0} em binário é: {1}' .format(n, bin(n)[2:]))
elif b == 'octal':
    print('O valor {0} em octal é: {1}' .format(n, oct(n)[2:]))
elif b == 'hexadecimal':
    print('O valor {0] em hexadecimal é: {1}' .format(n, hex(n)[2:]))
else:
    print('\033[31mvoce nao selecionou a base!')
