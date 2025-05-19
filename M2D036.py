# Financiamento da casa comparado ao salário
casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos voce quer parcelar? '))
if casa / (anos * 12) > 0.3 * salario:
    print('\033[1;31mSeu empréstimo foi negado\033[m')
else:
    print('\033[1;32mSeu empréstimo foi aceito\033[m\nSerao {0} parcelas de R${1:.2f}' .format(anos * 12, casa/(anos * 12)))
