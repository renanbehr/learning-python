# Exercício 61 Aula 14 - PA com while
t = int(input(print('Digite o 1º termo da PA: ')))
r = int(input(print('Digite a razão da PA: ')))
cont1 = 0
cont2 = int(input('Digite aqui quantos termos você quer ver: '))
while cont1 < cont2:
    print(t + (r * cont1))
    cont1 += 1
    if cont2 == 0:
        print('FIM')
print('FIM')
