# Exercício 75 Aula 16 - Insere valores e os define com Tuplas
lista = (int(input('Digite um valor inteiro: ')),
         int(input('Digite um valor inteiro: ')),
         int(input('Digite um valor inteiro: ')),
         int(input('Digite um valor inteiro: ')))
print(f'O número 9 aparece {lista.count(9)} vezes')
if 3 in lista:
    print(f'O número 3 aparece primeiro na {lista.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ')
for n in lista:
    if n % 2 ==0:
        print(n)
