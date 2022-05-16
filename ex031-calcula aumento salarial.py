# Exercício 34
wage = float(input('Digite seu salário e veja quanto ele será após o aumento: '))
if wage <= 1250.0:
    print(f'O aumento será de {wage * 0.15:.2f}')
    print(f'O seu salário passará a ser {wage * 1.15:.2f}')
else:
    print(f'O aumento será de {wage * 0.10:.2f}')
    print(f'O seu salário passará a ser {wage * 1.10:.2f}')
