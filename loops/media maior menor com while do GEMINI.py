lista = []

while True:
    try:
        num = int(input('Digite um número: '))
        lista.append(num) # Adiciona o número à lista imediatamente

        # Loop interno para garantir uma resposta válida para 'continuar'
        while True:
            try:
                continuar = int(input('Deseja continuar? [1] para sim [2] para não: '))
                if continuar == 1:
                    break # Sai do loop interno, continua o loop principal
                elif continuar == 2:
                    break # Sai do loop interno, e depois o loop principal será quebrado
                else:
                    print('Opção inválida! Digite 1 para sim ou 2 para não.')
            except ValueError:
                print('Entrada inválida para a opção! Por favor, digite 1 ou 2.')

        # Se o usuário escolheu '2' (não continuar), sai do loop principal
        if continuar == 2:
            break

    except ValueError:
        print('Entrada inválida para o número! Por favor, digite um número inteiro.')
        # Não adiciona nada à lista e volta para o início do loop principal

# --- Cálculo e Saída ---
# Verifica se a lista não está vazia antes de calcular a média
if lista:
    qtdelista = len(lista)
    soma = sum(lista)
    media = soma / qtdelista
    print(f'A média entre os {qtdelista} números digitados foi de {media:.2f}') # .2f para 2 casas decimais
    print(f'Os números digitados foram: {lista}')
else:
    print('Nenhum número foi digitado para calcular a média.')