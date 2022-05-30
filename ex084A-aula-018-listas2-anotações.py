# Exercício 84 Aula 18 - Anotações sobre Listas 2
'''
teste = list()
teste.append('Renan')
teste.append(27)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste, galera)
'''

'''
galera = ['joão', 19], ['ana', 33], ['joaquim', 53], ['maria', 57]
print(galera[0][0])
print(galera[3])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
'''

# esse codigo cria duas listas, uma pra captar dados e ser apagada
# e outra lista onde os dados ficam gravados e podem ser trabalhados
'''
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Há {totmai} pessoas maiores de idade e {totmen} menores de idade')
'''
