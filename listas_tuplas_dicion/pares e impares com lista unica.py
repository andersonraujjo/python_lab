

lista_unica = [[],[]]
for i in range (1,8):
    numero_usuario = int(input(f'Digite o {i}° valor: '))
    if numero_usuario %2 == 0:
        lista_unica[0].append(numero_usuario)
    else:
        lista_unica[1].append(numero_usuario)

lista_unica[0].sort()
lista_unica[1].sort()

print(f'Os numeros pares digitados em ordem crescente: {lista_unica[0]}')
print(f'Os ímpares: {lista_unica[1]}')



