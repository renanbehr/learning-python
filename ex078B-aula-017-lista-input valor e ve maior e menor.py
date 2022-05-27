# Exercício 78 Aula 17 - Input de números em lista e vê qual é maior e menor
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
n1 = max(valores)
n2 = min(valores)
print(valores)
print(f'Na {valores.index(n1)+1}ª posição encontrei o maior valor {n1}')
print(f'Na {valores.index(n2)+1}ª posição encontrei o menor valor {n2}')
