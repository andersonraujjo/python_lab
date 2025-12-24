


idadeslista = []
idadehv = 0
homemvelho = ''
mulheres20 = 0
for i in range (1,5):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M ou F): ').upper()
    idadeslista.append(idade)
    if sexo == 'M' and idade>idadehv:
        idadehv = idade
        homemvelho = nome
    if sexo == 'F' and idade <20:
        mulheres20 = mulheres20 + 1




soma = sum(idadeslista)
media = soma / 4




print(f'A média de idade desse grupo é de {media} anos!')
print(f'A idade do homem mais velho é de {idadehv} anos e ele se chama {homemvelho}!')
print(f'Ao todo são {mulheres20} mulheres abaixo de 20 anos!')

