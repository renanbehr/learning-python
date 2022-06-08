# Exercício 105 - Analisando e gerando dicionários com várias notas
def notas(*n, sit=False):
    """
    Função para analisar notas e situações de várias notas.
    :param n: uma ou mais notas (aceita várias)
    :param sit: valor opcional, indica se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre o aluno.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, sit=True)
print(resp)
