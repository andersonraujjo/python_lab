l1 = int(input('Digite o valor do lado 1: '))
l2 = int(input('Digite o valor do lado 2: '))
l3 = int(input('Digite o valor do lado 3: '))

if l1 + l2 > l3:
    print('é possivel formar um triângulo!')
else:
   print('não é possivel formar um triângulo!')

if l1 == l2 == l3:
    print('Será formado um triângulo equiilátero!')
if l1 != l2 !=l3:
    print('Será formado um triângulo escaleno!')
else:
    print('Será formado um triângulo isósceles!')

    