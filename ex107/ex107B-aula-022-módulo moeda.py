# Exercício 107 - Módulo Moeda
import moeda107
p = float(input('Digite um valor R$ '))
print(f'A metade de {p} é {moeda107.metade(p):.2f}')
print(f'O dobro de {p} é {moeda107.dobro(p):.2f}')
print(f'O aumento de 25 % de {p} é {moeda107.aumentar(p, 25):.2f}')
print(f'A diminuição de 30 % de {p} é {moeda107.diminuir(p, 30):.2f}')
