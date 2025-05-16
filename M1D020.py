# Aleatorizar uma lista com 4 alunos
from random import shuffle
a1 = input('Nome de um aluno: ')
a2 = input('Nome de outro aluno: ')
a3 = input('Nome de outro aluno: ')
a4 = input('Nome de mais um aluno: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A lista de alunos é:', alunos)
