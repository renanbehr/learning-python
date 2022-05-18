# Exercício 43 - Calcular IMC
peso = (float(input('Digite seu peso: ')))
alt = (float(input('Digite sua altura: ')))
imc = (peso / (alt * alt))
if 0 < imc <= 18.5:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso')
elif 18.5 < imc <= 25:
    print(f'Seu IMC é {imc:.2f} e você está no peso ideal')
elif 25 < imc <= 30:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade')
elif 30 < imc <= 40:
    print(f'Seu IMC é {imc:.2f} e você está obeso')
elif 40 < imc:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade mórbida')
else:
    print('Insira dados válidos')
