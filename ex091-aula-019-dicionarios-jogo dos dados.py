# Exercício 91 Aula 19 - Jogo dos dados
from random import randint
from operator import itemgetter
dados = dict()
dados['jogador1'] = randint(1, 6)
dados['jogador2'] = randint(1, 6)
dados['jogador3'] = randint(1, 6)
dados['jogador4'] = randint(1, 6)
ranking = list()
print('Valores sorteados: ')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('\n', '=' * 5, 'RANKING DOS JOGADORES', '=' * 5, '\n')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} tirou {v[1]}')
