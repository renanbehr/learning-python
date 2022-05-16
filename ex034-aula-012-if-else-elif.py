# Exercício 36
nome = str(input('Qual é o seu nome?')).strip().upper()
if nome == 'Renan'.upper():
    print('Que da hora')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'José'.strip().upper():
    print('Seu nome é bem comum no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana Camila Acarajéssica'.strip().upper():
    print('Que belo nome, moça!')
else:
    print('Seu nome é normal')
print(f'Tenha um bom dia, {nome}!')
