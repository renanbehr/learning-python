# Exercício 33
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
