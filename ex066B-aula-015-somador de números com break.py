# Exercício 66 Aula 15 - Anotações de Aula
n = s = cont = 0
while n != 999:
    n = int(input('Digite um número (O valor 999 para o contador): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Você somou {cont} números e a soma vale {s}')
