#PRÁTICA DA AULA 10 -> CONDIÇÃO COMPOSTA
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2)/2
print(f'A sua média foi {n}')
if n >= 6.0:
    print('A sua média foi boa e você foi aprovado!')
else:
    print('Você é um apedeuta e está reprovado!')

#PRÁTICA DA AULA 10 -> CONDIÇÃO SIMPLIFICADA
n3 = float(input('Digite a primeira nota: '))
n4 = float(input('Digite a segunda nota: '))
n5 = (n3 + n4)/2
print(f'A sua média foi {n5}')
print('A sua média foi boa e você foi aprovado' if n5 >= 6.0 else 'Você é um apedeuta e está reprovado!')
