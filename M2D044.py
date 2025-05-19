# Valor de um produto dependendo da forma de pagamento
v = float(input('Informe o valor do produto: R$'))
f = str(input('Agora informe sobre o metodo de pagamento: ')).lower().strip()
if f.find('cheque') == 0 or f.find('dinheiro') == 0:
    print('O valor a pagar será R${0:.2f}'.format(v * 0.9))
elif f.find('crédito') == 0 or f.find('credito') == 0:
    p = int(input('Informe a quantidade de parcelas: '))
    if 1 < p < 3:
        print('O valor total a ser pago será de R${0:.2f}'
              '\nEm {1} parcelas de R${2}' .format(v, p, v / p))
    elif p >= 3:
        print('O valor total a ser pago será de R${0:.2f}'
              '\nEm {1} parcelas de R${2}' .format(v * 1.2, p, v * 1.2 / p))
    elif p == 1:
        print('O valor total a ser pago será de R${0:.2f}'
              '\nEm {1} parcelas de R${2}' .format(v * 0.95, p, v * 0.95))
elif f.find('débito') == 0 or f.find('debito') == 0:
    print('O valor será R${0:.2f}' .format(v * 0.95))
elif f.find('cartão') == 0 or f.find('cartao') == 0:
    cd = str(input('Será crédito ou débito? ')).lower().strip()
    if cd.find('crédito') == 0 or cd.find('credito') == 0:
        c = int(input('Quantas parcelas? '))
        if c == 1:
            print('O valor a ser pago será de R${0:.2f}'.format(v * 0.95))
        if 1 < c < 3:
            print('O valor total a ser pago será de R${0:.2f}'
                  '\nEm {1} parcelas de R${2}'.format(v, c, v / c))
        elif c >= 3:
            print('O valor total a ser pago será de R${0:.2f}'
                  '\nEm {1} parcelas de R${2}'.format(v * 1.2, c, v * 1.2 / c))
        else:
            p = int(input('Informe a quantidade de parcelas: '))
            if 0 < p < 2:
                print('''O valor total a ser pago será de R${0:.2f}
                Em {1} parcelas de R${2}'''.format(v, p, v / p))
            elif p <= 3:
                print('''O valor total a ser pago será de R${0:.2f}
                      Em {1} parcelas de R${2}}'''.format(v * 1.2, c, v * 1.2 / c))
    elif cd.find('débito') == 0 or cd.find('debito') == 0:
         print('O valor será {0:.2f}'.format(v * 0.95))
