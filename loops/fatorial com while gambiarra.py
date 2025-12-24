

from math import prod



num = int(input('Digite o numero: '))
contador = num
lista = [num]


while contador >0:
    contador = contador - 1
    lista.append(contador)

lista.remove(0)

f = prod(lista)


print(f'O fatorial de {num} é {f}')
print(lista)

    