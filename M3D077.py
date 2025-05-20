#Tupla com várias palavras (sem acentos) mostrar para cada palavra quais sao suas respectivas vogais
lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programar', 'futuro')
for c in range(0, len(lista)):
    e = lista[c]
    vogais = ''
    for d in range(0, len(e)):
        if e[d] == 'a':
            vogais += 'a'
        elif e[d] == 'e':
            vogais += 'e'
        elif e[d] == 'i':
            vogais += 'i'
        elif e[d] == 'o':
            vogais += 'o'
        elif e[d] == 'u':
            vogais += 'u'
    print(f'A palavra {e.upper()} possui as vogais {vogais.upper()}')
