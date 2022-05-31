# Exercício 88 Aula 18 - Gerador de jogo da Mega Sena
from random import randint
jogo = [0, 0, 0, 0, 0, 0]
numjogos = int(input('Digite quantos jogos você quer que eu sorteie: '))
for x in range(1, numjogos+1):
    jogo[0] = randint(1, 60)
    jogo[1] = randint(1, 60)
    jogo[2] = randint(1, 60)
    jogo[3] = randint(1, 60)
    jogo[4] = randint(1, 60)
    jogo[5] = randint(1, 60)
    jogo.sort()
    print(f'Jogo {x}: {jogo}')
