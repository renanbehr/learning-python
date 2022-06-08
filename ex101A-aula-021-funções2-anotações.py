# Anotações Aula 21 - Funções 2
# Interactive help -> help()
# Docstrings -> cria interactive help


def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c<=f:
        print(f'{c} ', end='')
        c+=p
    print('FIM')


print('Exemplo de de criação de docstrings e interactive help')
help(contador)
contador(0, 10, 2)
print('')
# Parâmetros opcionais


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


print('Exemplo de Parâmetros opcionais')
somar(1, 2, 3)
somar(1, 2)
somar(1)
somar()
print('')
# Escopo de variáveis


def funcao():
    n1 = 4
    print(f'N1 local vale {n1}')


n1 = 2
print('Exemplo de Escopo de variáveis')
funcao()
print(f'N1 global vale {n1}')
print('')

# Retorno de Resultados


def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s


print('Exemplo de Retorno')
r1 = somar2(3, 2, 5)
r2 = somar2(1, 7)
r3 = somar2(4)
print(f'Meus cálculos deram {r1}, {r2}, {r3}.')
r4 = r1 + r2 + r3
print(f'A soma das somas é igual a {r4}.')
print('')
# Exemplos


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}.')
print('')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('DIgite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
