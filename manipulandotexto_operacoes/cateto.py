import math
c1 = int(input('Digite a área do primeiro cateto: '))
c2 = int(input('Digite a área do segundo cateto: '))
h = (c1**2 + c2**2)
hf = math.sqrt(h)
print(f'A hipotenusa desse triângulo é de {hf}')