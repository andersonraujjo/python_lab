import random

numero = random.randint(1,10)
tentativas = 0
t = 0
while t != numero:
    t = int(input('Tente adivinhar um numero de 1 a 10: '))
    tentativas = tentativas + 1
if tentativas == 1:
    print('Você acertou de primeira, parabéns!')
print(f'Você acertou o número escolhido pela máquina, o {numero}, depois de {tentativas} tentativas!')
