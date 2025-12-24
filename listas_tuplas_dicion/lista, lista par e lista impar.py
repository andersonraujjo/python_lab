




lista_completa = []
lista_pares = []
lista_impares = []

while True:
    entrada_usuario = int(input('Digite um numero: '))
    lista_completa.append(entrada_usuario)
    if entrada_usuario %2 ==0:
        lista_pares.append(entrada_usuario)
    else:
        lista_impares.append(entrada_usuario)

    while True:
        escolha_usuario = input('Deseja continuar? [S/N]: ').upper()
        if escolha_usuario in 'SN':
            break
        else:
            print('Opção invalida.')
    
    if escolha_usuario == 'N':
        break

print(f'A lista completa de todos os numeros é {lista_completa}')
print(f'A lista com todos os pares é {lista_pares}')
print(f'A lista com todos os impares: {lista_impares}')

