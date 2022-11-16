def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de alunos.
    :param n: uma ou mais notas de alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionario com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r


#Programa principal
resp = notas(2.5, 5.8, 7.2, 1.1, sit=True)
print(resp)
help(notas)
