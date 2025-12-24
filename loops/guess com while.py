import random
num = random.randint(1,10)
tent = 0
n = 0
while n != num:
    n = int(input('Digite um numero de 1 a 10: '))
    if n != num:
        print('Você errou! Tente novamente!')
        tent = n+1
    else:
        print(f'Parabéns, você acertou! A quantidade de erros desse jogo foi de {tent} tentativas!')