# Exercício 97 - Aula 20 - Função print especial GUANABARA
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)


# Programa principal
escreva('Renan Maia Behr da Rocha')
escreva('CAMILA')
escreva('CeV')
