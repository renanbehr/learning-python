# Exercício 81 Aula 17 - Lista com sort inverso e contador
lista = []
while True:
    r = str(input('Você quer adicionar um valor à lista? [S/N] '))
    if r in 'Ss':
        lista.append(int(input('Adicione um valor à lista: ')))
    elif r in 'Nn':
        break
    else:
        print('Digite uma resposta válida.')
print(f'Você digitou {len(lista)} números na lista.')
lista.sort(reverse=True)
print(f'Os seguintes números foram digitados: {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
