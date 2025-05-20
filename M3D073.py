#Tupla do brasileirao com 4 opçoes, 5 primeiros, 4 ultimos, ordem alfabética e posiçao do chapecoense
lista = ('athletico-pr', 'bahia', 'flamengo', 'botafogo', 'sao paulo', 'cruzeiro', 'atlético-mg', 'bragantino', 'palmeiras', 'internacional', 'fortaleza', 'gremio', 'vasco', 'criciuma', 'juventude', 'corinthians', 'fluminese', 'vitoria', 'atletico-go', 'cuiaba')
while True:
    print('[A] para ver os 5 primeiros colocados')
    print('[B] para ver os últimos 4 colocados')
    print('[C] para ver a lista em ordem alfabética')
    print('[D] para localizar a posicao do chapecoense')
    print('[E] para sair do console')
    resposta = input(str('Digite a opçao: ')).upper().strip()
    if resposta == 'A':
        print(lista[0:5])
    if resposta == 'B':
        print(lista[-4:0])
    if resposta == 'C':
        print(sorted(lista)) #organiza a lista em ordem alfabética
    if resposta == 'D':
        if ('chapecoense' in lista) is True:
            print(f'O Chapecoense está na {lista.index("chapecoense")+1} posiçao') #nao me lembro o comando para localizar
        else:
            print('Chapecoense nao esta na lista')
    if resposta == 'E':
        break
