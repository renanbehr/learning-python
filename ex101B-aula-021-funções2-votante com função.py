# Exercício 101 - Função para votantes
def voto(nasc):
    idade = 2022 - nasc
    if 65 > idade > 18:
        return print('VOTO OBRIGATÓRIO')
    elif 16 > idade > 0:
        return print('VOTO NEGADO')
    elif 0 > idade:
        return print('VISITANTES DO FUTURO NÃO PODEM VOTAR')
    else:
        return print('VOTO OPCIONAL')


nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
