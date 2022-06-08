# Anotações Aula 23 - Tratamento de erros e exceções
# As funções try, except são obrigatórias; else, finally são opcionais
try:
    a = float(input('NUmerador: '))
    b = float(input('Denominador: '))
    r = a/b
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
   print(f'Problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado!')
