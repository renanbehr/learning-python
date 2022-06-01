# Exercício 94 Aula 19 - Estatística de pessoas - RENAN
pessoal = list()
individuo = dict()
tot_idade = 0
tot_cadastro = int(input('Quantas pessoas você deseja cadastrar? '))
for c in range(0, tot_cadastro):
    individuo['Nome'] = str(input(f'Qual o nome da pessoa {c+1}? '))
    individuo['Idade'] = int(input(f'Qual a idade da pessoa {c+1}? '))
    individuo['Sexo'] = str(input(f'Qual o sexo da pessoa {c+1} [M/F] ? '))
    tot_idade += individuo['Idade']
    pessoal.append(individuo.copy())
media = tot_idade / tot_cadastro
print(f'Foram cadastradas {tot_cadastro} pessoas.')
print(f'A idade média das {tot_cadastro} pessoas castradas é de {media} anos.')
