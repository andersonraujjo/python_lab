

from math import prod

lista = []

n = int(input('Digite um numero: '))


for i in range(n,0,-1):
    lista.append(i)
    f = prod(lista)


print(f'O fatorial do numero {n} é igual a {f}!')
print(f"""O resultado se obtem multiplicando todos os numeros de {n} a 1: 
{lista}""")
