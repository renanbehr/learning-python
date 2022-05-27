# Exercício 78 Aula 17 - Anotações sobre Listas
'''num = [2, 3, 9, 1, 4, 4, 4]
num[2] = 1
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(f'{v}...',)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')'''

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontrei o valor {v}...')'''

#Este comando deste jeito cria uma ligação entre as duas e faz com que ambas sejam sempre iguais
'''a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B {b}')'''

#Este comando cria uma cópia perfeita de uma lista que pode ser alterada depois sem alterar a lista original
'''a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B {b}')'''
