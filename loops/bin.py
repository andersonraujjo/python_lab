lista = [10, 15, 23, 65, 72, 88, 91]
alvo = 88

inicio = 0
fim = len(lista) - 1

while inicio <= fim:
    meio = (inicio + fim) // 2  # divide a soma toda

    if lista[meio] == alvo:
        print(f"Encontrado na posição {meio}")
        break

    elif lista[meio] < alvo:
        inicio = meio + 1  # joga fora a metade esquerda

    else:
        fim = meio - 1     # joga fora a metade direita
else:
    print("Número não encontrado")