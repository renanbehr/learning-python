# Exercício 76 Aula 16 - Lista de Preços com Tupla
lista = ('Lápis', 0.99,
         'Borracha', 1.99,
         'Caderno', 15.99,
         'Estojo', 24.99,
         'Transferidor', 4.99,
         'Compasso', 9.99,
         'Mochila', 119.99,
         'Canetas', 4.99,
         'Livro', 39.99)
print('-' * 30)
print(f'{"NOTA FISCAL":^30}')
print('-' * 30)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-' * 30)
