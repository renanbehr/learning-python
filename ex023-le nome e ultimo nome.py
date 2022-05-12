# Exercício 27
a = (input('Diga seu nome: ')).strip()
b = a.split()
print(f'Seu primeiro nome é {b[0]}')
print(f'Seu último nome é {b[len(b)-1]}')
