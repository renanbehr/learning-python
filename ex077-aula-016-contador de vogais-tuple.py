# Exercício 76 Aula 16 - Contador de vogais com Tupla
palavras = ('CAMILA', 'RENAN', 'ALAN', 'RODOLFO', 'MARIA',
         'EDUARDA', 'JULIA', 'ALBERTO', 'TADEU', 'JUNIOR',
         'NARCIZO', 'ANTERO', 'ANGELINA', 'DANIELA')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
