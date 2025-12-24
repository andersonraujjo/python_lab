



lista_matriz = []
dados = []
for i in range (1,10):
    entrada_usuario = int(input(f'Digite um numero para a posição {i}: '))
    dados.append(entrada_usuario)
    if len(dados) ==3:
        lista_matriz.append(dados[:])
        dados.clear()

print(f'{lista_matriz[0]}\n{lista_matriz[1]}\n{lista_matriz[2]}')