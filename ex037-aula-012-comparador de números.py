# Exercício 38 Comparador de números
n1 = float(input('Insira o 1º valor: '))
n2 = float(input('Insira o 2º valor: '))
n3 = float(input('Insira o 3º valor: '))
if n1 > n2 and n1 > n3:
    print(f'O 1º valor: {n1} é o maior valor')
elif n2 > n1 and n2 > n3:
    print(f'O 2º valor: {n2} é o maior valor')
elif n3 > n1 and n3 > n2:
    print(f'O 3º valor: {n3} é o maior valor')
elif n3 == n2 == n1:
    print('Não existe valor maior, os três valores são iguais')
