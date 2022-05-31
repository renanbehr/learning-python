# Exercício 90 Aula 19 - Boletim lê média e dá a situação do aluno
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-=' * 16)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
