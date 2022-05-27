# Exercício 79 Aula 17 - Input de números em lista que adiciona só valores diferentes
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado.')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Você digitou os seguintes valores {sorted(numeros)}')
