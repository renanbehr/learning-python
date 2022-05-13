# Exercício 33
from datetime import date
ano = int(input('Digite um ano ou digite 0 para o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano informado é bissexto')
else:
    print('O ano informado não é bissexto')
