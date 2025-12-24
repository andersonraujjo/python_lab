


def leiaInt (msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print('ERRO! Digite um número inteiro.')
        

n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')