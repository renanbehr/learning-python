import math
an = float(input('Digite o ângulo que vc deseja: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print(f'O seno é {se:.2f}, o cosseno é {co:.2f}, e a tangente é {ta:.2f}')
