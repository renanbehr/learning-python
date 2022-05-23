# Exercício 59 Aula 14 - Calculadora
print('Bem vindo à calculadora do Renan!')
opt = 0
while opt != 5:
    n1 = float(input('Digite aqui o primeiro número: '))
    n2 = float(input('Digite aqui o segundo número: '))
    opt = int(input('''
    ***** OPÇÕES *****
    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - QUAL O MAIOR?
    [4] - REDEFINIR NÚMEROS
    [5] - SAIR
    '''))
    if opt == 1:
        print(f'A soma de {n1} e {n2} é igual a {n1 + n2}')
    elif opt == 2:
        print(f'A multiplicação de {n1} vezes {n2} é igual a {n1 * n2}')
    elif opt == 3 and n1 > n2:
        print(f'O valor {n1} é maior que {n2}')
    elif opt == 3 and n1 == n2:
        print('Ambos os valores são iguais!')
    elif opt == 3 and n2 > n1:
        print(f'O valor {n2} é maior que {n1} ')
print('Até logo!')
