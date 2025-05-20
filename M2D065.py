#Média dos números + maior e menor
r = ''
maior = 0
menor = 0
s = 0
count = 0
total = 0
while s != 1:
    n = int(input('Digite um número: '))
    total += n
    if n > maior:
        maior = n
    if count == 0:
        menor = n
    elif count != 0:
        if n < menor:
            menor = n
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if r == 'S':
        s = 0
    elif r == 'N':
        s = 1
    else:
        print('\033[31mOpcao nao escolhida, irei continuar\033[m')
    count += 1
print('A média entre todos os números digitados foi {0}, o maior número é {1} e o menor número é {2}'
      .format((total / count), maior, menor))
