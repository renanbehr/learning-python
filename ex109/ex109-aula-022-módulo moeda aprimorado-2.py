import moeda109
p = float(input('Digite um valor R$ '))
print(f'A metade de {moeda109.moeda(p)} é {moeda109.metade(p, True)}')
print(f'O dobro de {moeda109.moeda(p)} é {moeda109.dobro(p, True)}')
print(f'O aumento de 25 % de {moeda109.moeda(p)} é {moeda109.aumentar(p, 25, True)}')
print(f'A diminuição de 30 % de {moeda109.moeda(p)} é {moeda109.diminuir(p, 30, True)}')
