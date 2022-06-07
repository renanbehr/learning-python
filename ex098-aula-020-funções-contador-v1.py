# Exercício 98 - Aula 20 - Função Contador RENAN
def contador(i, f, p):
    if f > 0:
        f += 1
    else:
        f -= 1
        if p > 0:
            p *= -1
    if p == 0:
        p += 1
    for c in range(i, f, p):
        print(c, end=' ')


# Programa principal
print('\nVamos contar de 1 a 10: ')
contador(1, 11, 1)
print('\nAgora de 10 a 0 de 2 em 2: ')
contador(10, -1, -2)
print('\nAgora sua contagem personalizada!')
i = int(input('Digite um número inicial: '))
f = int(input('Digite um número final: '))
p = int(input('Digite o passo da contagem: '))
contador(i, f, p)
