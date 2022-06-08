# Exercício 102 - Fatorial
def fatorial(n=1, show=False):
    """
    Programa serve pra calcular o fatorial de determinado número inteiro e natural.
    :param n: número inteiro e natural que terá o fatorial calculado.
    :param show: (opcional) se True, mostra o cálculo, se False mostra nada.
    :return: retorna o fatorial do número n.
    """
    f = 1
    print(f'O fatorial de {n} é: ', end='')
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
print(fatorial(0, show=True))
print(fatorial(10, show=False))
print(fatorial(2))
print(fatorial(16))
print(fatorial(100, show=True))
help(fatorial)
