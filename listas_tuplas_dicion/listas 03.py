


lista = []

while True:
    entrada_usuario = int(input('Digite um numero: '))
    lista.append(entrada_usuario)
    while True:
        escolha_usuario = input('Deseja continuar? [S/N]: ').upper()
        if escolha_usuario in 'SN':
            break
        else:
            print('Opção inválida.')
    if escolha_usuario == 'N':
        break

lista.sort(reverse=True)
print(f'Ao todo foram digitados {len(lista)} numeros!')
print(f'A lista ordenada de forma decrescente é: {lista}')
if 5 in lista:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O numero 5 não foi digitado nennhuma vez.')



