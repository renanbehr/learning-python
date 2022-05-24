# Exercício 65 Aula 14 - Média entre vários números
soma = 0
cont = 0
num = 0
confirma = ''
maior = 0
menor = 10000
while confirma in 'sS':
    num = int(input('Digite o número a ser somado: '))
    soma += num
    cont += 1
    confirma= (str(input('Você quer digitar mais um número? [S / N]')))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
if confirma in 'Nn':
    print(f'A média deu {soma / cont}.')
    print(f'Você somou {cont} números.')
    print(f'O maior número foi {maior} e o menor foi {menor}.')
else:
    print('Insira os valores corretamente.')
