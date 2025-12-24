



def ficha (nome,gols):
    
    if not nome:
        nome = '<desconhecido>'
    
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    
    
jogador = str(input('Digite o nome do jogador: '))
g = input('Quantos gols: ')

print(ficha(jogador,g))
