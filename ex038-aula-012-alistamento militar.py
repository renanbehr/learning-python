# Exercício 39 Alistamento militar
from datetime import date
atual = date.today().year
nasc = int(input('Diga qual o ano em que vc nasceu: '))
idade = atual - nasc
if 18 < idade < 120:
    print(f'Você tem {idade} anos e sua época de alistamento foi a {idade - 18} anos atrás.')
elif idade == 18:
    print(f'Você está com {idade} anos e deve se alistar neste ano.')
elif 0 <= idade <= 4:
    print(f'Você é um bebê ainda, não há por que se preocupar com isto agora.')
elif idade < 0:
    print(f'Ha ha ha, muito engraçado! Diga realmente o ano em que nasceu.')
elif idade >= 120:
    print(f'Como é a vida após a morte?')
else:
    print(f'Você possui {idade} anos e só irá se alistar daqui a {18 - idade} anos.')
