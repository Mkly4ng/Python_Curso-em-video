# Calcular o IMC e a categoria que se encaixa
print('Informe o peso e a altura para calcular o IMC')
p = float(input('Peso (kg): '))
a = float(input('Altura (m): '))
print('Seu IMC é {0:.1f}' .format(p / a ** 2))
if p / a ** 2 < 18.5:
    print('\033[33mAbaixo do peso')
elif 18.5 <= p / a ** 2 < 25:
    print('\033[032mPeso ideal')
elif 25 <= p / a ** 2 < 30:
    print('\033[33mSobrepeso')
elif 30 <= p / a ** 2 < 40:
    print('\033[31mObesidade')
elif 40 <= p / a ** 2:
    print('\033[31mOBESIDADE MÓRBIDA')
