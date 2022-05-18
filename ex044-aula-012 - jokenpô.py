# Exercício 44 - Jokenpô
import random
print('-='*31)
print('Bem vindo ao JOKENPÔ! O computador vai escolher a jogada dele.')
pc = random.randint(1, 3)
user = int(input('Digite aqui qual a sua jogada, sendo:\n'
                 '1 - PEDRA\n'
                 '2 - PAPEL\n'
                 '3 - TESOURA\n'
                 '4 - SAIR DO JOGO\n '
                 'Sua escolha é: '))
print('-='*31)
if pc == 1 and user == 1:
    print('Você empatou com a máquina! Os dois escolheram PEDRA.')
elif pc == 1 and user == 2:
    print('Você ganhou! A máquina escolheu PEDRA e você escolheu PAPEL.')
elif pc == 1 and user == 3:
    print('Você perdeu! A máquina escolheu PEDRA e você escolheu TESOURA.')
elif pc == 2 and user == 1:
    print('Você perdeu! A máquina escolher PAPEL e você escolheu PEDRA.')
elif pc == 2 and user == 2:
    print('Você empatou com a máquina! Os dois escolheram PAPEL.')
elif pc == 2 and user == 3:
    print('Você ganhou! A máquina escolheu PAPEL e você escolheu TESOURA.')
elif pc == 3 and user == 1:
    print('Você ganhou! A máquinha escolheu TESOURA e você escolheu PEDRA.')
elif pc == 3 and user == 2:
    print('Você perdeu! A máquina escolheu TESOURA e você escolheu PAPEL.')
elif pc == 3 and user == 3:
    print('Você empatou com a máquina! Os dois escolheram TESOURA.')
else:
    print('Até a próxima!')
