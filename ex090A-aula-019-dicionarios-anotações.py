# Exercício 90 Aula 19 - Anotações sobre Dicionários
''' tuplas ()
    lista []
    dicionários {}'''

'''dados = dict() ou dados = {'nome': 'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade']
dados['sexo']='M'
deldados['idade']'''

'''filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filme.values()) -> print = Star Wars, 1977, George Lucas
print(filme.keys()) -> print = titulo, ano, diretor
print(filme.items()) -> print = tudo
for k, v in filme.items():
    print(f'O (k) é (v)')'''

'''pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 27}
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.values())
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''pessoas = {'nome': 'Camila', 'sexo': 'F', 'idade': 26}
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''pessoas = {'nome': 'Renan', 'sexo': 'M', 'idade': 27}
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 111.11
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = list()
estado1 = {'uf': 'Distrito Federal', 'sigla': 'DF'}
estado2 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])'''

'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil: #laço de fora para a lista
    for k, v in e.items(): #laço de dentro para dicionario
        print(f'O campo {k} tem valor {v}')'''

'''from random import randint
from operator import itemgetter # esse comando dessa lista serve para ordenar os itens de um dicionário
dados = dict()
dados['jogador1'] = randint(1, 6)
dados['jogador2'] = randint(1, 6)
dados['jogador3'] = randint(1, 6)
dados['jogador4'] = randint(1, 6)
ranking = list()
print('Valores sorteados: ')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True) # o intemgetter transforma o dicionário em uma lista, pegando os dados da 2ª posição e joganod numa lista e ordenando eles.
print('\n', '=' * 5, 'RANKING DOS JOGADORES', '=' * 5, '\n')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} tirou {v[1]}')'''
