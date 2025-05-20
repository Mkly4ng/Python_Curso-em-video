#Todos exceto 999
n = 0
n1 = 0
count = 0
while n != 999:
    n = float(input('Digite os números que deseja somar, para encerrar digite 999: '))
    n1 += n
    count += 1
print('Parabéns voce acertou depois de {0} números e a soma total foi de {1}' .format(count - 1, n1-n))
