from moedapasta import moeda


#preco = float(input('Digite o preço: R$'))
preco = moeda.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco,20,30)



#print(f'A metade de {moeda.cifrao(preco)} é igual a {moeda.cifrao(moeda.metade(preco))}')
#print(f'O dobro de {preco} é igual a {moeda.dobro(preco)}')
#print(f'Aumentando {preco} em 15% por cento: {moeda.aumentar(preco,15)}')
#print(f'Diminuindo {preco} em 10%: {moeda.diminuir(preco,10)}')