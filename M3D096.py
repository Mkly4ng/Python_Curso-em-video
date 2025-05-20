#Criar uma funçao para o calculo de área => area()
def area(l, c):
    a = l * c
    print(f'A área do quadrado de comprimento {c}m e largura {l}m vale {a}m2')


l = float(input('Digite a largura em metros: '))
c = float(input('Digite o comprimento em metros: '))
area(l, c)
