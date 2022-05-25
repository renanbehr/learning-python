# Exercício 68 Aula 15 - Par ou ímpar contra a máquina, break = derrota do usuário
import random
print('-=' * 20)
print('JOGO DE PAR OU ÍMPAR')
print('-=' * 20)
cont = 0
while True:
    user = int(input('Diga um valor: '))
    pi = str(input('Par ou ímpar? [P / I] ')).strip().upper()[0]
    pc = random.randint(0, 10)
    soma = user + pc
    while pi not in 'PI':
        pi = str(input('Par ou ímpar? [P / I] ')).strip().upper()[0]
    if soma % 2 == 0 and pi in 'Pp':
        print(f'Você jogou {user} e a máquina {pc}, a soma é {soma}')
        print(f'{soma} é par!')
        print('Você venceu! Vamos jogar novamente!')
    elif soma % 2 != 0 and pi in 'Ii':
        print(f'Você jogou {user} e a máquina {pc}, a soma é {soma}')
        print(f'{soma} é ímpar!')
        print('Você venceu! Vamos jogar novamente!')
    else:
        break
    cont += 1
print(f'Você jogou {user} e a máquina jogou {pc}'
      f'\nGAME OVER! Você ganhou {cont} vezes da máquina.')
