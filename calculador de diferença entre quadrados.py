# Calculador da diferença entre quadrados perfeitos
n = 0
n1 = 1
r = 50
print('n1 ao quadrado: ')
for n in range(r):
    print(n ** 2, end=' ')
    n += 1
    n1 += 1
print('')
print('n2 ao quadrado: ')
n = 0
n1 = 1
for n in range(r):
    print(n1 ** 2, end=' ')
    n += 1
    n1 += 1
print('')
print('diferença entre os n: ')
n = 0
n1 = 1
for n in range(r):
    print(n1 ** 2 - n ** 2, end=' ')
    n += 1
    n1 += 1
