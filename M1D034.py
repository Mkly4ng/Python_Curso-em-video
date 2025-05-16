# Aumento percentual do salário conforme o valor
s = float(input('Qual é o seu salário? R$'))
if s <= 1250:
    print('Seu salário terá um aumento de 15%, assim ficando R${0:.2f}' .format(s * 1.15))
else:
    print('Seu salário terá um aumento de 10%, assim ficando R${0:.2f}' .format(s * 1.1))

