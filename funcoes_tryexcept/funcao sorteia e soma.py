

import random


lista = []
def sorteia():
    for i in range (5):
        num = random.randint(0,100)
        lista.append(num)
    print(lista)

listapar = []
def somapar():
    for i in lista:
        if i %2 == 0:
            listapar.append(i)
    print(f'A soma dos pares {listapar} é {sum(listapar)}')

print('-'*30)
sorteia()
print('-'*30)
somapar()



