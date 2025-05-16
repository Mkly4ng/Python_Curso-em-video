# Primeiro e ultimo nome
n = str(input('Digite seu nome completo: ')).strip()
s = n.split()
print('''Primeiro nome = {0}
Último nome = {1}''' .format(s[0], s[len(s)-1]))
