# Exercício 33, Update exercício 42
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
    if r1 == r2 == r3:
        print('Este é um triângulo EQUILÁTERO')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Este é um triângulo ESCALENO')
    else:
        print('Este é um triângulo ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
