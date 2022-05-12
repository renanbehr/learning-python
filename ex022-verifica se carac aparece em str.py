# Exercício 26
a = (input('Diga uma frase: ')).upper().strip()
print(f'A letra "a" aparece {a.count("A")} vez(es)')
print('A primeira letra A apareceu na posição {}'.format((a.find('A')+1)))
print('A letra A aparece pela última vez na posição {}'.format((a.rfind('A')+1)))
