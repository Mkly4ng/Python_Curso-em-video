# Funçao notas(), vai ler inúmeras notas e devolver a quant, maior, meor, média e situacçao (opicional) + docstrings
def notas(*n, sit=False):
    """
    => Função para analisar a situação de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou n!ao adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    count = total = 0
    for a in n:
        count += 1
        total += a
        print(a)
        if a == n[0]:
            maior = menor = a
        else:
            if a > maior:
                maior = a
            if menor > a:
                menor = a
    result = dict()
    result['total'] = count
    result['maior'] = maior
    result['menor'] = menor
    result['média'] = (total / count)
    if sit is True:
        if (total / count) > 7:
            result['situação'] = 'BOA'
        if 6 <= (total/count) < 7:
            result['situação'] = 'RAZOÁVEL'
        if (total/count) < 6:
            result['situação'] = 'RUIM'
    for a, i in result.items():
        print(f'{a}: {i}, ', end='')


notas(1, 2, 3, 4, 5, 6)
