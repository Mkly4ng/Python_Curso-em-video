# verificar se tem silva no  nome
n = str(input('Escreva seu nome: ')).strip()
u = n.upper()
s = u.split()
print('SILVA' in s)
#print('Seu nome tem Silva? {}' .format('silva' in n.lower()))
