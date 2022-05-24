# Exercício 63 Aula 14 - Sequência de Fibonacci
anterior = 0
proximo = 0
n = int(input('Digite quantos termos você quer ver:'))
cont = 0
while cont <= n:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    cont += 1
    if proximo == 0:
        proximo = proximo + 1
print('FIM')
