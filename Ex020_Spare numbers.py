# Exercício 23
o = int(input('Diga um número de 0 a 9999: '))
u = o // 1 % 10
d = o // 10 % 10
c = o // 100 % 10
m = o // 1000 % 10
print(f'Analisando o número {o}...')
print(f'Milhar {m}')
print(f'Centena {c}')
print(f'Dezena {d}')
print(f'Unidade {u}')
