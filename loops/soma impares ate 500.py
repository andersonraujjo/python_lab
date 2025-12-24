soma = 0
cont = 0
for i in range (1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
        cont = cont + 1
print(f'A soma de todos os {cont} valores é de {soma}')


#soma = soma + i pode ser chamado também com soma += i
#cont + 1 = contar a quantidade de numeros dentro da variavel