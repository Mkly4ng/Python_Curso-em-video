# Quant de "A" e a posiçao do primeiro e último
f = str(input('Escreva uma frase: ')).strip()
u = f.upper()
print('''A sua frase tem {0} A
O primeiro A aparece em {1}
O ultimo A aparece em {2}''' .format(u.count('A'), u.find('A')+1, u.rfind('A')+1))
