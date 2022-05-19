# Exercício 49 Aula 13 - Tabuada com laço
n = int(input(print('Digite um número: ')))
print(f'TABUADA DO {n}')
for c in range(1, 11):
    print(f'{n} x {c} = {c * n}')
print('FIM')
