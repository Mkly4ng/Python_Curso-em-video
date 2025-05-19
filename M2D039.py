# Alistamento em relacao a idade
from datetime import date
d = int(input('Informe a sua data de nascimento: '))
data = date.today().year
if data - d == 18:
    print('Voce tem que se alistar esse ano')
elif data - d < 18:
    print('Voce tera que se alistar daqui {0} anos' .format(18 - data + d))
elif data - d > 18:
    print('Voce tinha que ter se alistado a {0} anos atrás' .format(data - d - 18))
