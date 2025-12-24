vel = int(input('Digite a velocidade do carro: '))
#calculo velocidade acima do limite
val = vel -80
#velocidade acima x multa de 7 reais
vm = val * 7
if vel >= (81):
    print(f'Você ultrapassou a velocidade permitida da via! O valor da multa a ser cobrado é de {vm} reais!')
else:
    print('Você está dentro do limite da via, continue assim!')
