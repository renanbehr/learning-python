# Exercício 90 Aula 19 - Boletim lê média e dá a situação do aluno
nome = str(input('Digite o nome do aluno: '))
media = float(input(f'Digite a média de {nome}: '))
sit = ''
if media >= 7:
    sit = 'Aprovado!'
elif media >= 5:
    sit = 'Recuperação'
else:
    sit = 'Reprovado'
dados = {'Nome': nome, 'Média': media, 'Situacao': sit}
print('-=' * 18)
print(f' - nome é igual a {nome}')
print(f' - média é igual a {media}')
print(f' - situação é igual a {sit}')
