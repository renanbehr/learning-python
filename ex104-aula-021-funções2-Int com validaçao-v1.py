# Exercício 104 - Função que lê inteiros
def LeiaInt(num=''):
    while num is not int:
        num = str(input('Digite um número inteiro: '))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Digite um número inteiro válido!')
    return num


n = LeiaInt()
print(f'Você digitou o número {n}')
