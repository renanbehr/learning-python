# Exercício 72 Aula 16 - Escreve o número por extenso
lista = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', \
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {lista[num]}')
        loop = str(input('Quer continuar novamente? [S/N] ')).strip().upper()
        if loop[0] in 'N':
            print('Até a próxima!')
            break
    else:
        print('Tente novamente. ', end='')
