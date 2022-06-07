# Exercício 98 - Aula 20 - Função Contador GUANABARA
def contador(i, f, p):
    if p < 0:
        p += 1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print('FIM')
    else:
        cont = 1
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
        print('FIM')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Início: '))
fin = int(input('Final: '))
pas = int(input('Passo: '))
contador(ini, fin, pas)
