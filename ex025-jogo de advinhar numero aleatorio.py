# Exercício 28
import random
print('Bem vindo ao jogo da Advinhação! \n'
      'O computador escolherá um númeo de 0 a 5. Advinhe o número!')
a = random.randint(0, 5)
b = int(input('Digite aqui qual o número que o computador escolheu: '))
print('Parabéns! Você é sortudo!'if a == b else 'Não foi desta vez!')
print(f'O número escolhido pelo computador foi {a}')
