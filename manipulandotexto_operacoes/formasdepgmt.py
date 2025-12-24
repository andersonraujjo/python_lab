valorproduto = int(input('Digite o valor do produto: '))

formapgto = int(input("""Digite um número equivalente a forma de pagamento do produto:
Á vista dinheiro ou cheque: 1
Á vista no cartão: 2
Até 2x no cartão: 3
3x ou mais: 4 = """))

avistadesc = valorproduto * 0.10
avistacartdes = valorproduto * 0.05
tresvezesjur = valorproduto * 0.20

finalavista = valorproduto - avistadesc
finalavistacart = valorproduto - avistacartdes
finaltresvezes = valorproduto + tresvezesjur

if formapgto ==1:
    print(f'A forma de pagamento será a vista/cheque e você irá obter 10% de desconto no produto. O valor total ficará em {finalavista:.0f}, com {avistadesc:.0f} de desconto!')
elif formapgto ==2:
    print('A forma de pagamneto será a vista no cartão e você  irá obter 5% de desconto no produto. O valor total ficará em {finalavistacart:.0f}, com {avistacartdes:.0f} de desconto!')
elif formapgto ==3:
    print(f'A forma de pagamento será em até duas vezes no cartão. O valor total será de {valorproduto:.0f} sem alterações!')
else:
    print(f'A forma de pagamento será em 3x ou mais no cartão, acrescido de 20% de juros sobre o valor total do produto ({valorproduto:.0f}). O valor final será de {finaltresvezes:.0f}')
