# Exercício 57 Aula 14 - Digite o sexo e recuse valores != de M, F
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    if sexo in 'M':
        print('Seu dado foi registrado com sucesso, senhor.')
    elif sexo in 'F':
        print('Seu dado foi registrado com sucesso, senhora.')
    else:
        print('Insira os dados corretamente.')
print('********** FIM DE TRANSMISSÃO **********')
