def aumentar(quant=0.0, aum=0.0, formato=False):
    p = quant + ((aum / 100) * quant)
    return p if formato is False else moeda(p)


def diminuir(quant=0.0, dim=0.0, formato=False):
    p = quant - ((dim / 100) * quant)
    return p if formato is False else moeda(p)


def dobro(quant=0.0, formato=False):
    p = quant * 2
    return p if formato is False else moeda(p)


def metade(quant=0.0, formato=False):
    p = quant/2
    return p if formato is False else moeda(p)


def moeda(quant=0.0, moeda='R$'):
    return f'{moeda} {quant:.2f}'.replace('.', ',')


def resumo(quant=0.0, aum=0.0, dim=0.0):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(quant)}')
    print(f'Dobro do preço: \t{dobro(quant, True)}')
    print(f'Metade do preço: \t{metade(quant, True)}')
    print(f'{aum} % de aumento: \t{aumentar(quant, aum, True)}')
    print(f'{dim} % de redução: \t{diminuir(quant, dim, True)}')
    print('-' * 30)
