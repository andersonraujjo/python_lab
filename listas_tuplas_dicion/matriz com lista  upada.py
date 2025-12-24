



lista_matriz = []
dados = []
soma_pares = 0
soma_3coluna = 0
maior_valor_2linha = 0

for i in range (1,10):
    entrada_usuario = int(input(f'Digite um numero para a posição {i}: '))
    dados.append(entrada_usuario)
    if entrada_usuario %2 ==0:
        soma_pares += entrada_usuario
    if len(dados) ==3:
        lista_matriz.append(dados[:])
        dados.clear()


for l in lista_matriz[1]:
    if maior_valor_2linha == 0:
        maior_valor_2linha = l
    if l > maior_valor_2linha:
        maior_valor_2linha = l


for l in lista_matriz:
    soma_3coluna += l[2]

print(f'O maior valor da segunda linha é o {maior_valor_2linha}')
print(f'A soma da 3 coluna é igual a {soma_3coluna}')
print(f'A soma de todos os pares digitados é {soma_pares}')
print(f'{lista_matriz[0]}\n{lista_matriz[1]}\n{lista_matriz[2]}')