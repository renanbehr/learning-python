# Exercício 84 Aula 18 - Lista com nomes e pesos de pessoas
galera = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso: ')))
    if len(galera) ==0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(galera)} pessoas.')
print(f'O maior peso foi {maior}')
for p in galera:
    if p[1] == maior:
        print(f'A pessoa mais pesada foi [{p[0]}]')
print(f'O menor peso foi {menor}')
for p in galera:
    if p[1] == menor:
        print(f'A pessoa mais leve foi [{p[0]}]')
