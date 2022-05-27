# Exercício 74 Aula 16 - Maior e menor números com Tuplas
from random import randint
lista = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))
print(f'Os 5 valores sorteados foram {lista}')
print(f'O menor valor sorteado foi {min(lista)}')
print(f'O maior valor sorteado foi {max(lista)}')
