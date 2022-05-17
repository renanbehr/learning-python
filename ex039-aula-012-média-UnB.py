# Exercício 40 Cálculo da Menção
n1 = float(input('Insira aqui a sua 1ª nota: '))
n2 = float(input('Insira aqui a sua 2ª nota: '))
n3 = float(input('Insira aqui a sua 3ª nota: '))
n4 = float(input('Insira aqui a sua 4ª nota: '))
me = (n1 + n2 + n3 + n4) / 4
if me >= 9.0:
    print(f'Excelente! Sua nota foi {me:.2f} e sua menção foi SS!')
elif 9.0 >= me >= 7.0:
    print(f'Muito bom! Sua nota foi {me:.2f} e sua menção foi MS.')
elif 7.0 >= me >= 5.0:
    print(f'Você passou na matéria, com nota {me:.2f} e menção MM.')
elif 5.0 >= me >= 3.0:
    print(f'Você não passou, sua nota foi {me:.2f} e sua menção MI.')
elif 3.0 >= me > 0.0:
    print(f'Você não passou, sua nota foi {me:.2f} e sua menção foi II.')
elif me == 0.0:
    print(f'Você não só não passou, como sua nota foi {me:.2f}. Sua menção é SR.')
