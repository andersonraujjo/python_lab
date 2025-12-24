frase = input('Digite a frase: ').lower().replace(' ','')
frasecontr = frase[::-1]
print(f'O inverso de {frase} é {frasecontr}!')
if frasecontr == frase:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')