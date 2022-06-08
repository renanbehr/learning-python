def aumentar(quant=0, aum=0, formato=False):
    p = quant + ((aum / 100) * quant)
    return p if formato is False else moeda(p)


def diminuir(quant=0, dim=0, formato=False):
    p = quant - ((dim / 100) * quant)
    return p if formato is False else moeda(p)


def dobro(quant=0, formato=False):
    p = quant * 2
    return p if formato is False else moeda(p)


def metade(quant=0, formato=False):
    p = quant/2
    return p if formato is False else moeda(p)


def moeda(quant=0.0, moeda='R$'):
    return f'{moeda} {quant:.2f}'.replace('.', ',')
