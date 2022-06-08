# Exercício 103 - Ficha de Jogadores
def ficha(jog='<Desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')


n = str(input('Digite o nome do jogador: '))
g = str(input('Digite quantos gols o jogador fez no campeonato: ')) #
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    n = '<Desconhecido>'
ficha(n, g)
