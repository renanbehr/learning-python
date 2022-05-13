# Exercício 29
print('Bem vindo, infrator! \n'
      'Digite a velocidade a qual você trafegava!')
a = int(input('Insira velocidade: '))
b = a - 80
if a <= 80:
    print('Hoje você não foi multado!')
else:
    print(f'Você será multado em R$ {b * 7:.2f}')
