jogador = dict()
lista_gols = []
lista_jogadores = []

while True:
    jogador['nome'] = input('Qual o nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou: '))
    
    for partida in range(jogador['partidas']):
        lista_gols.append(int(input(f'Quantos gols {jogador['nome']} fez na partida {partida}: ')))
    jogador['gols'] = lista_gols[:]
    
    lista_jogadores.append(jogador.copy())
    jogador.clear()
    lista_gols.clear()

    while True:
        resposta_usuario = str(input('Deseja continar? [S/N]: ')).upper()
        if resposta_usuario in 'SN':
            break
        print('Opção inválida.')
    if resposta_usuario == 'N':
        break

print('__'*30)
for jogadores in range(len(lista_jogadores)):
    print(f'Cod = {jogadores} | Nome = {lista_jogadores[jogadores]['nome']} | Gols = {lista_jogadores[jogadores]['gols']} | Total = {sum(lista_jogadores[jogadores]['gols'])}')

print('__'*30)

while True:
    num_jogador = int(input('Mostrar levantamento de qual jogador (cod) [999 interrompe]: '))
    if num_jogador == 999:
        break
    if num_jogador > len(lista_jogadores) -1:
        print('Opção inválida. Não há jogador com esse código.')
    
    if num_jogador <= len(lista_jogadores) - 1:
        print(f'Levantamento do jogador {lista_jogadores[num_jogador]['nome']}')
        for i,k in enumerate((lista_jogadores[num_jogador]['gols'])):
            print(f'No jogo {i} ele fez {k} gols.')
       
print('__'*30)

