q = float(input('Informe a quilometragem rodada: '))
d = int(input('Informe a quantidade de dias do aluguel: '))
print(f'A quantia devida do aluguel do veículo é de R${d*60+q*0.15}, sendo R${d*60}'
      f' pelos dias e R${q*0.15} pela quilometragem rodada')
