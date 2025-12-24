



listagem_precos = ('Pão', 7.50, 'Arroz', 20.90, 'Leite', 5.10, 'Ovo', 13.99, 'Manteiga', 8.99)


print('_'*50)
print('LISTAGEM DE PREÇOS')
print('_'*50)

#print(listagem_precos[0], end=' '), print('.'*10,end=' '), print('R$',listagem_precos[1])
#print(listagem_precos[2], end=' '), print('.'*10,end=' '), print('R$',listagem_precos[3])

contagem_itens = int(len(listagem_precos)) 
cont = 0
for i in range (0, contagem_itens):
    print(listagem_precos[cont], end=' '), print('.'*10,end=' ')
    cont += 1
    print('R$',listagem_precos[cont])
    cont += 1
    if cont ==10:
        break

print('_'*50)