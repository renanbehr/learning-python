# Exercício 73 Aula 16 - Tabela do Brasileiro 2021 com tuplas
tabela = 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',\
         'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',\
         'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',\
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense'
print(f'Os 5 primeiro colocados foram {tabela[:5]}')
print(f'Os 4 times rebaixados foram {tabela[16:]}')
print(f'Os times em ordem alfabética são {sorted(tabela)}')
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')
