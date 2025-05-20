# Tabuada usando laço "for"
n = float(input('Digite o número que deseja saber a tabuada: '))
for c in range(0,11):
    print('{0:2} x {1} = {2}' .format(c, n, c * n))
