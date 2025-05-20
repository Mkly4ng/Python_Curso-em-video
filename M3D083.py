#Adicionar uma expresao algébrica numa lista e verificar o uso dos parenteses
lista = []
countl = 0
countr = 0
expressao = str(input('Digite a expressao númerica: '))
lista.append(expressao)
for n in expressao:
    if n == '(':
        countl += 1
    if n == ')':
        countr += 1
if countl == countr:
    print('O uso do parentese está \033[32mcorreto\033[m')
else:
    print('O uso do parentese está \033[31merrado\033[m')
