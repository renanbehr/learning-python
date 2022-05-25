# Exercício 69 Aula 15 - Cadastro de pessoas com break
print('Cadastrador de pessoas')
maiores = mulheres = homens = 0
while True:
    sexo = str(input('Diga seu sexo [M / F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Diga seu sexo [M / F]: ')).strip().upper()[0]
    idade = int(input('Diga sua idade: '))
    continuar = str(input('Continuar cadastrando? [S / N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Continuar cadastrando? [S / N]: ')).strip().upper()[0]
    if sexo in 'Mm':
        homens += 1
    if idade >= 18:
        maiores += 1
    if sexo in 'Ff' and idade <= 20:
        mulheres += 1
    if continuar in 'Nn':
        break
print(f'Você cadastrou: {homens} homens, {maiores} pessoas com mais de 18 anos e {mulheres} mulheres com menos de 20 anos.')
