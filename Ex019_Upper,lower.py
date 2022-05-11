# Exercício 22
a = (input('Diga seu nome competo: '))
print(f'O nome em maiúsculas é {a.upper()}')
print(f'O nome em minúsculas é {a.lower()}')
b = a.replace(' ', '')
print(f'O total de caracteres sem os espaços no nome é: {len(b)}')
print(f'O total de caracteres com os espaços no nome é: {len(a)}')
c = a.split()
print(f'O total de caracteres do 1º nome é {len(c[0])}')
