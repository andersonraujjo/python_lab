import random
def adivinha(x):
    random_number = random.randint(1,x)
    adivinha = 0
    while adivinha != random_number:
        adivinha = int (input (f'Adivinhe um numero entre 1 e {x}: ' ))
        if adivinha < random_number:
            print ('Muito baixo. Tente de novo')
        elif adivinha > random_number:
            print ('Muito alto. Tente de novo')

    print (f'Parabéns, você acertou o número', random_number, 'corretamente!')

adivinha(10)
