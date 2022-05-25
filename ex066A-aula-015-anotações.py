# Exercício 66 Aula 15 - Anotações de Aula
n = s = 0
cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
print(cont)
print(f'A soma vale {s}')
