

lista = []

while True:
    entrada_usuario = int(input('Digite um valor: '))
    
    if entrada_usuario in lista:
        print('Numero já adicionado.')
    else:
        lista.append(entrada_usuario)
        print('Valor adicionado com sucesso')
    
    while True:
        escolha_usuario = input('Deseja continuar? [S/N]: ').upper()
        if escolha_usuario in 'SN':
            break
        else:
            print('Opção invalida')
    if escolha_usuario == 'N':
        break

lista.sort()
print(f'Lista ordenada: {lista}')




