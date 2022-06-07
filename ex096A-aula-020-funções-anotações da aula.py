# Aula 20 - Anotações sobre Funções em Python
# Funções são trechos de código que podem ser executados em momentos
# diferentes de nossos códigos em Python.
# Veja como funciona o comando def em Python e como utilizá-lo com
# parâmetros simples e múltiplos.
"""def soma(a, b): #definição da função
    s = a + b
    print(s)


# Programa principal
soma(a=4, b=5)
soma(b=8, a=9)
soma(94, 95)"""

'''def soma(a, b):
    print(f'A = {a}, B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
soma(a=4, b=5)
soma(b=8, a=9)
soma(94, 95)'''

# conceito de empacotamento
''''def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''


# conceito de desempacotamento
'''def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)'''
