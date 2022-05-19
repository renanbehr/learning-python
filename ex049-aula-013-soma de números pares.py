# Exercício 50 Aula 13 - Soma de 6 números pares
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(print('Digite um número: ')))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números pares e a soma deles deu {soma}')
