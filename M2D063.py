#Sequencia de Fibonacci
n1 = int(input('Informe o primeiro termo da sequencia de fibonacci: '))
quant = int(input('Informe a quantidade de elementos da sequencia: '))
q = 0
t = 0
t1 = 0
lista = []
while q != quant:
    if q == 0:
        t = n1
        t1 = t
        q += 1
        lista.append(t1)
        print(t1, end=' ')
    else:
        t = t1 - t
        t1 = t + t1
        q += 1
        lista.append(t1)
        print(t1, end=' ')
print(lista)
