# Exercício 41 Confederação de Natação
from datetime import date
atual = date.today().year
nasc = int(input('Insira aqui o seu ano de nascimento: '))
idade = atual - nasc
if idade > 100:
    print('Poxa, tem piscina aí no céu?')
elif 100 > idade > 25:
    print(f'Você tem {idade} e está na categoria MASTER')
elif 25 > idade > 19:
    print(f'Você está com {idade} anos e está na categoria SÊNIOR')
elif 19 > idade > 14:
    print(f'Você está com {idade} anos e está na categoria JÚNIOR')
elif 14 > idade > 9:
    print(f'Você está com {idade} anos e está na categoria INFANTIL')
elif 9 > idade > 0:
    print(f'Você está com {idade} anos e está na categoria MIRIM')
elif 0 > idade:
    print('Poxa, você nem nasceu ainda e já quer nadar!?')
