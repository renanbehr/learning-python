# Exercício 48 Aula 13 - Soma dos números ímpares múltiplos de 3
soma = 0
cont = 0
for c in range(3, 501, 6):
    print(c)
    cont += 1
    soma += c
print(f'O somatório de todos os {cont} múltiplos de 3 ímpares é {soma}')
