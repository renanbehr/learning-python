# Exercício 64 Aula 14 - Somador de números exceto o 999
soma = 0
cont = 0
num = 0
while num != 999:
    num = int(input('Digite o número a ser somado: '))
    soma += num
    cont += 1
    if num == 999:
        print(f'A soma deu {soma - 999}.')
        print(f'Você somou {cont - 1} números.')
