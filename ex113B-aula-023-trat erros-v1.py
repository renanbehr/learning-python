# ex113 - LeiaInt e LeiaFloat
def LeiaInt(i=0):
    while True:
        try:
            i = int(input('Digite um número inteiro: '))
            break
        except:
            print('Por favor, digite um número inteiro válido!')
    return i


def LeiaFloat(f=0):
    while True:
        try:
            f = float(input('Digite um número real: '))
            break
        except:
            print('Por favor, digite um número real válido!')
    return f


print(f'O valor inteiro digitado foi {LeiaInt()} e o real foi {LeiaFloat()}')
