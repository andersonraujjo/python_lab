d = int(input('Digite a distância da sua viagem: '))

#ate 200
a = d / 2

#apos 200
a1 = 0.45 * d

if d <= 200:
    print(f'o preço da passagem é {a}!')
elif d >= 200:
    print(f'O valor da passagem será de {a1}!')

          
