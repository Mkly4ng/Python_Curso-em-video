# se o aluno passou de ano a partir da média das notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
if (n1 + n2) / 2 < 5:
    print('\033[31mREPROVADO')
elif 7 > (n1 + n2) / 2 >= 5:
    print('\033[33mRECUPERAÇÃO')
elif (n1 + n2) / 2 >= 7:
    print('\033[32mAPROVADO')
