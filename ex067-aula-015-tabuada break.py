# Exercício 67 Aula 15 - Tabuada só encerra com break de número negativo
cont = 0
print('Digite um número e veja sua tabuada! Número negativo para o contador.')
n = int(input('Digite um número: '))
while cont < 10:
    if n < 0:
        break
    cont += 1
    print(f'{n} x {cont} = {n * cont}')
    if cont == 10:
        n = int(input('Digite um número: '))
        cont = 0
print('FIM DO PROGRAMA')
