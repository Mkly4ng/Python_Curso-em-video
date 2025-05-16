# Quantidade de dólares compráveis a partir de determinado capital
n = float(input('Informe o valor atual: R$'))
dc = n/3.27
d = 3.27
print(' Saldo atual: R${0} \n Preco do dolar: US${1} \n Quantidade de dolar compravel: US${2:.2f}' .format(n, d, dc))
