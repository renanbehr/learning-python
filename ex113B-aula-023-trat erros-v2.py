# ex113 - LeiaInt e LeiaFloat - GUANABARA
def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados encerrada pelo usuário!')
            return 0
        else:
            return n


def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número real válido!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados encerrada pelo usuário!')
            return 0
        else:
            return n


num = LeiaInt('Digite um valor inteiro: ')
mun = LeiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {mun}')
