#Função escreva() que receba uma mensagem e mostre com tamanho variável
def escreva(txt):
    n = len(txt)
    print('~'*(len(txt) + 2))
    print(f' {txt:}')
    print('~'*(len(txt) + 2))


msg = str(input('Digite uma mensagem: '))
escreva(msg)
