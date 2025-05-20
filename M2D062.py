#Melhorando o desafio D061
p1 = float(input('Digite o primeiro termo da P.A.: '))
r = float(input('Digite o valor da razao: '))
count = 0
pa = []
while count != 10:
    pa.append(p1 + (r * count))
    count += 1
print('Os 10 primeiros termos da P.A. sao {0}' .format(pa))
q = str(input('Deseja adicinar mais termos? [S/N]: ')).strip().upper()
quant = 0
if q == 'S':
    while q == 'S':
        quant = int(input('Quantos termos serao adicionados? '))
        #print(count)
        n1 = count + quant
        while count != n1:
            pa.append(p1 + (r * count))
            count += 1
            #print(count)
        print('A P.A com os novo(s) {0} membro(s) é {1}' .format(quant, pa))
        q = str(input('Deseja adicionar mais termos? [S/N]: ')).strip().upper()
    print(count)
elif q == 'N':
    print(count)
