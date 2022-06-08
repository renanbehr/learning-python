import moeda108
p = float(input('Digite um valor R$ '))
print(f'A metade de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.metade(p))}')
print(f'O dobro de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.dobro(p))}')
print(f'O aumento de 25 % de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.aumentar(p, 25))}')
print(f'A diminuição de 30 % de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.diminuir(p, 30))}')
