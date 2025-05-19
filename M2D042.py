# Se é possível formar um triangulo e qual tipo de triangulo é
n1 = float(input('Informe o valor do primeiro lado: '))
n2 = float(input('Informe o valor do segundo lado: '))
n3 = float(input('Informe o valor do terceiro lado: '))
if n1 != 0 and n2 != 0 and n3 != 0:
    if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
        print('Os seguintes valores podem formar um triangulo')
        if n1 == n2 == n3:
            print('O triangulo sera equilátero')
        elif n1 != n2 != n3 != n1:
            print('O triangulo sera escaleno')
        elif n1 == n2 != n3 or n2 == n3 != n1 or n1 == n3 != n2:
            print('O Triangulo sera isósceles')
    else:
        print('Os valores {0}, {1}, {2} nao podem formar um triangulo' .format(n1, n2, n3))
else:
    print('\033[31mUm dos valores foi informado errado')
