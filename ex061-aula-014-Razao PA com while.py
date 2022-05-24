# Exercício 61 Aula 14 - PA com while
t = int(input(print('Digite o 1º termo da PA: ')))
r = int(input(print('Digite a razão da PA: ')))
cont = 0
while cont <= 10:
    print(t + (r * cont))
    cont += 1
print('FIM')
