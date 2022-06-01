# Exercício 92 Aula 19 - Dicionário que aponta com quantos anos a pessoa aposenta
nome = str(input('Digite seu nome: '))
nasc = int(input('Digite seu ano de nascimento: '))
idade = 2022 - nasc
ctps = int(input('Digite aqui a sua carteira de trabalho:[0 se não possuir] '))
dados = {'Nome': nome, 'Ano de nascimento': nasc, 'Idade': idade, 'CTPS': ctps}
if ctps != 0:
    trabalho = int(input('Digite o ano de sua contratação: '))
    salario = float(input('Digite aqui o seu salário: '))
    temposervico = 2022 - trabalho
    aposentadoria = 40 - temposervico
    idadeaposentadoria = idade + aposentadoria
    dados = {'Nome': nome, 'Ano de nascimento': nasc, 'Idade': idade, 'CTPS': ctps, 'Salário': salario, 'Idade de aposentadoria': idadeaposentadoria}
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
