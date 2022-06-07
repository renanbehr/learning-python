# Exercício 100 - Aula 20 - Função que sorteia números
from random import randint


def sorteia(lista):
   print('Sorteando 5 valores da lista: ', end='')
   for cont in range(0, 5):
       n = (randint(0, 10))
       lista.append(n)
       print(f'{n} ', end='')
   print('\nPRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
print(numeros)
somaPar(numeros)
