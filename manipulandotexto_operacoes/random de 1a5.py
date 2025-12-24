import random
n = int(input('Adivinhe o numero que a maquina escolheu: '))
na = random.randint(1,5)
if n == na:
    print('Parabéns, você acertou o número!')
else:
    print('Você errou, a máquina venceu!')
    