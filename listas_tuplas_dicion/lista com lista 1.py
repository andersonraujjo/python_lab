
pessoas = list()
dados = []
maior_peso = menor_peso = 0 
#loop inicial para add as listas
while True:

    dados.append(str(input('Qual o nome: ')))
    dados.append(int(input('Qual o peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]

    pessoas.append(dados[:])
    dados.clear()

#loop para verificar se o usuario deseja continuar
    while True:
        resposta_usuario = input('Deseja continuar? [S/N]: ').upper()
        if resposta_usuario in 'SN':
            break
        else:
            print('Opção inválida')

    if resposta_usuario == 'N':
        break

print(f'O maior peso foi de {maior_peso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ',end='')

    
print(f'\nO menor peso foi de {menor_peso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')



print(f'\nAo todo foram cadastradas {len(pessoas)} pessoas.')

