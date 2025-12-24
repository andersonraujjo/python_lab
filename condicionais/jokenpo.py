import random

print('Bem vindo ao jogo JOKENPÔ! Você deverá escolher entre pedra, papel ou tesoura e a máquina irá jogar contra você aleatóriamente!')
print("\n")


usuario = input('Digite P para pedra, PA para papel e T para tesoura: ').upper()

lista = ['Pedra', 'Papel', 'Tesoura']
maquina = random.choice(lista)

print("\n")
print(f'Decisão da máquina: {maquina}')
print("\n")

if usuario == 'P' and maquina == 'Tesoura':
    print('Você ganhou! Pedra ganha de tesoura!')
elif usuario == 'P' and maquina == 'Papel':
    print('Você perdeu! Pedra perde para papel!')
elif usuario == 'P' and maquina == 'Tesoura':
    print('Empate! Tente de novo!')


if usuario == 'PA' and maquina == 'Pedra':
    print('Você ganhou! Papel ganha de pedra!')
elif usuario == 'PA' and maquina == 'Tesoura':
    print('Você perdeu! Tesoura ganha de papel!')
elif usuario == 'PA' and maquina == 'Papel':
    print('Empate! Tente novamente!')


if usuario == 'T' and maquina == 'Pedra':
    print('Você perdeu! Tesoura perde para pedra!')
elif usuario == 'T' and maquina == 'Papel':
    print('Você ganhou! Tesoura ganha de papel!')
elif usuario == 'T' and maquina == 'Tesoura':
    print('Empate! Tente novamente!')

print("\n")
