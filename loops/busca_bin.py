lista = [1, 3, 5, 7, 9, 11] # Ordenada!
alvo = 7
inicio, fim = 0, len(lista) - 1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        print(f"Encontrado no índice {meio}")
        break
    elif lista[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1