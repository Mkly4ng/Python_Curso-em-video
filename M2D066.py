#Recebe número, faz a soma e indica quantos números
n = count = total = 0
while True:
    n = float(input('Digite m número: '))
    if n == 999:
        break
    total += n
    count += 1
print(f'A soma total foi {total} e foram digitados {count} números')
