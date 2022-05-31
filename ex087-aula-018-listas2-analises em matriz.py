# Exercício 87 Aula 18 - Matriz 3x3 analisada
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior2 = coluna3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}] [{c}]: '))
        if matrix[l][c] % 2 == 0:
            par += matrix[l][c]
        if matrix[l][2]:
            coluna3 += matrix[l][2]
        if matrix[1][c] > maior2:
            maior2 = matrix[1][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
print(f'A soma dos números pares da matriz é igual a {par}')
print(f'A soma dos valores da 3ª coluna é igual a {coluna3}')
print(f'O maior valor da 2ª linha é o número {maior2}')
