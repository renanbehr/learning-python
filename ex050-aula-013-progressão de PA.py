# Exercício 51 Aula 13 - Progressão da PA
t = int(input(print('Digite o 1º termo da PA: ')))
r = int(input(print('Digite a razão da PA: ')))
t10 = t + (10 - 1) * r
for c in range(t, t10 + r, r):
    print(c)
print('FIM')
