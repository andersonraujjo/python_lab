




lista_matriz = [[], [], []]
for i in range (1,4):
    num1 = int(input(f'Digite um valor para 0,{i}: '))
    lista_matriz[0].append(num1)

for c in range (1,4):
    num2 = int(input(f'Digite um valor para 1,{c}: '))
    lista_matriz[1].append(num2)

for h in range (1,4):
    num3 = int(input(f'Digite um valor para 2,{h}: '))
    lista_matriz[2].append(num3)
    

print(lista_matriz[0])
print(lista_matriz[1])
print(lista_matriz[2])