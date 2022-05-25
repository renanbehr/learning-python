# Exercício 70 Aula 15 - Caixa automático lê prod + barato e soma valores
print('Caixa automático')
soma = 0
nomebarato = ''
valorbarato = 999
caros = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    valor = float(input('Digite o valor do produto: '))
    soma += valor
    if valor < valorbarato:
        nomebarato = nome
        valorbarato = valor
    if valor > 1000:
        caros += 1
    continuar = str(input('Quer continuar sua compra? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar sua compra? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'Sua compra deu R$ {soma:.2f}')
print(f'Você comprou {caros} produtos que custam mais de R$ 1000')
print(f'{nomebarato} foi o produto mais em conta da lista, por apenas R$ {valorbarato:.2f}')
