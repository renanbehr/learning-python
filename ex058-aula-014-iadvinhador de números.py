# Exercício 58 Aula 14 - Refazendo jogo da advinhação ex 28
import random
print('Bem vindo ao jogo da Advinhação! \n'
      'O computador escolherá um número de 0 a 10. Advinhe o número!')
pc = random.randint(0, 10)
cont = 0
user = 11
while user != pc:
    user = int(input('Digite aqui qual foi o número que o computador pensou: '))
    cont += 1
    if user < pc:
        print('Mais... Tente de novo!')
    elif user > pc:
        print('Menos... Tente de novo!')
print(f'Parabéns! Você conseguiu vencer a máquina! E só levou {cont} tentativas!')
