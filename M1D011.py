# Quantidade de tinta necessaria para pintar uma parede, baseado na largura, comprimento e redimento do litro de tinta
l = float(input('Informe a largura da parede: '))
c = float(input('Informe o comprimento da parede: '))
a = l*c
r = float(input('Informe o rendimento do litro de tinta por metro quadrado: '))
q = a/r
print('A partir da largura e comprimento informados, a área da parede é de {0} metros quadrados \nCom um rendimento de {1} metros quadrados por litro, sáo necessários {2} litros de tinta' .format(a, r ,q))
