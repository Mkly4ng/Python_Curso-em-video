# Tabuada de vários números, para quando for negativo
while True:
    print('=' * 30)
    n = int(input('Digite o valor a ser visto na tabuada: '))
    print('=' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:2} = {n * c}')
print('\033[32mObrigado por usar a tabuada!\033[m')
