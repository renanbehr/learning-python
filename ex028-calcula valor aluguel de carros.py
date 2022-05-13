# Exercício 31
a = float(input('Informe a distância da viagem: '))
if a <= 200:
    print(f'O valor da passagem para a viagem de {a} é R$ {a * 0.50:.2f}')
else:
    print(f'O valor da passagem para a viagem de {a} é R$ {a * 0.45:.2f}')
