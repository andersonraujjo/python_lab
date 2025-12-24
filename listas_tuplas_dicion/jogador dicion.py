


jogador = dict()

jogador['nome'] = input('Qual o nome do jogador: ')
jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou: '))
lista_gols = []

for i in range (jogador['partidas']):
    lista_gols.append(int(input(f'Quantos gols na partida {i}: ')))

jogador['gols'] = lista_gols
jogador['totalgols'] = sum(lista_gols)

print('-'*30)
for key, values in jogador.items():
    print(f'O campo {key} tem o valor {values}')

print('-'*30)
print(f'O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.')
for i,v in enumerate(lista_gols):
    print(f'Na partida {i}, fez {v} gols.')
    
