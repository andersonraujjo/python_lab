

lista = []
for i in range (0,6):
    entrada_usuario = int(input(f'Digite um valor para a posição {i}: '))
    lista.append(entrada_usuario)
    numeromaior = max(lista)
    numeromenor = min(lista)

print('Você digitou os valores', lista)

for c, v in enumerate(lista):
    if v == numeromaior:
        print(f'Na posição {c} o maior valor digitado foi o {v}!')
    if v == numeromenor:
        print(f'Na posição {c} o menor valor digitado foi o {v}!')