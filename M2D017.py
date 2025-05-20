# Caixa eletronico
from math import trunc
valor = float(input('Qual valor voce deseja scar? R$'))
v50 = trunc(valor / 50)
v20 = trunc((valor - (50 * v50)) / 20)
v10 = trunc((valor - (50 * v50 + 20 * v20)) / 10)
v1 = trunc((valor - (50 * v50 + 20 * v20 + 10 * v10)) / 1)
print('=' * 30)
if v50 != 0:
    print(f'Total de {v50} cédulas de RS50')
if v20 != 0:
    print(f'Total de {v20} cédulas de R$20')
if v10 != 0:
    print(f'Total de {v10} cédulas de R$10')
if v1 != 0:
    print(f'Total de {v1} cédulas de RS1')
print('=' * 30)
print('Volte sempre! =D')
