# Exercício 44 - Opções de pgto de produto
preco = float(input('Digite o preço do produto: '))
forma = int(input('Insira a forma de pagamento sendo:\n'
                  '1 - DINHEIRO\n'
                  '2 - CHEQUE\n'
                  '3 - CARTÃO\n'
                  '4 - CANCELAR '))
if forma == 3:
    parcelamento = int(input('A compra será parcelada em quantas vezes? '))
    if parcelamento == 1:
        print(f'O produto sairá com um desconto de 5% por R$ {preco * 0.95:.2f}')
    elif parcelamento == 2:
        print(f'O produto sairá pelo preço normal, R$ {preco:.2f}')
    elif parcelamento >= 3:
        print(f'O produto será parcelado com juros de 20% e sairá por R% {preco * 1.20:.2f}')
elif forma == 1 or forma == 2:
    print(f'O produto sairá com um desconto de 10% por R$ {preco * 0.9:.2f}')
elif forma == 4:
    print('Foi um prazer atendê-lo! Espero que você nos procure caso mude de ideia!')
else:
    print('Por favor, insira os dados conforme intruções!')
