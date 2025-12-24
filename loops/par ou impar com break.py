



import random

jogadas = -1

while True:
    maquina = random.randint(1,10)
    jogador = int(input('Digite um numero para jogarmos par ou ímpar: '))
    escolha = input('Par ou Ímpar? [P ou I] ').upper()
    jogadas = jogadas + 1
    soma = maquina + jogador
        
    print('__'*15)
    print(f'A maquina jogou {maquina}!')
    print('__'*15)
    print(f'A soma de {maquina} + {jogador} é {soma}!')
    print('__'*15)


    if escolha == 'P' and soma % 2 == 0:
        print('Você ganhou!')
        print('__'*15)

    elif escolha == 'I' and soma % 2 == 1:
        print('Você ganhou!')
        print('__'*15)
    
    else:
        break
            

print('GAME OVER')
print(f'Você venceu um total de {jogadas} vezes consecutivas!')
print('\n')






