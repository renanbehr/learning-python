def aumentar(quant=0, aum=0):
    return quant + ((aum / 100) * quant)


def diminuir(quant=0, dim=0):
    return quant - ((dim / 100) * quant)


def dobro(quant=0):
    return quant * 2


def metade(quant=0):
    return quant/2


def moeda(quant=0, moeda='R$'):
    return f'{moeda} {quant:.2f}'.replace('.', ',')
