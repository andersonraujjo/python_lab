from moedapasta import moeda


valor = float(input('Digite um numero: '))

print('-'*30)
print(f'O dobro de {moeda.cifrao(valor)} é {moeda.dobro(valor,b=True)}')
print(f'A metade de {moeda.cifrao(valor)} é {moeda.metade(valor,True)}')
print(f'Aumentando em 10% o valor de {moeda.cifrao(valor)} temos {moeda.aumentar(valor,True)}')
print(f'Reduzindo o valor de {moeda.cifrao(valor)} em 13% temos {moeda.diminuir(valor,True)}')
print('-'*30)


#print(f'O dobro de {moeda.cifrao(valor)} é {moeda.cifrao(moeda.dobro(valor))}')
#print(f'A metade de {moeda.cifrao(valor)} é {moeda.cifrao(moeda.metade(valor))}')
#print(f'Aumentando em 10% o valor de {moeda.cifrao(valor)} temos {moeda.cifrao(moeda.aumentar(valor))}')
#print(f'Reduzindo o valor de {moeda.cifrao(valor)} em 13% temos {moeda.cifrao(moeda.diminuir(valor))}')
