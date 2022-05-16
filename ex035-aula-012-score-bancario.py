# Exercício 36 Analisador de empréstimo
valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual a sua renda mensal? '))
per = int(input('Em quantos anos você pretende pagar a casa? '))
pgto = valor / (per * 12)
if pgto > (sal * 0.3):
    print(f'Infelizmente a sua renda mensal de R$ {sal:.2f} não comporta o'
          f' pagamento da parcela mensal de R$ {pgto:.2f}')
else:
    print(f'Parabéns! Seu empréstimo foi autorizado e sua parcela mensal'
          f' será de R$ {pgto:.2f}')
