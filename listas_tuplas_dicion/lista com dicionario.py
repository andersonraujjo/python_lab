dicionario = {}
pessoas_lista = []
idades = 0
lista_mulheres = []
lista_acima_media = []
while True:
    dicionario['nome'] = str(input('Qual o nome: '))
    dicionario['sexo'] = str(input('Qual o sexo [M/F]: ')).upper()
    dicionario['idade'] = int(input('Qual a idade: '))
    idades += dicionario['idade']
    pessoas_lista.append(dicionario.copy())
    dicionario.clear()
    
    while True:
        resposta_usuario = input('Deseja continuar? [S/N]: ').upper()
        if resposta_usuario in 'SN':
            break
        print('Opção inválida.')
    if resposta_usuario == 'N':
        break

for i in pessoas_lista:
    if i['idade'] > idades/len(pessoas_lista):
        lista_acima_media.append(i)
    if i['sexo'] == 'F':
        lista_mulheres.append(i['nome'])
print('-'*30)

print(f'Ao todo foram cadastradas {len(pessoas_lista)} pessoas.')
print(f'A média de idade do grupo é de {idades/len(pessoas_lista):.2f}')
if len(lista_mulheres) > 0:
    print(f'As mulheres cadastradas foram: {lista_mulheres}')

print('-'*30)
if len(lista_acima_media) > 0:
    print(f'Lista das pessoas que estão acima da média: ')
    for i in lista_acima_media:
        print(f'Nome = {i['nome']}, Sexo = {i['sexo']}, Idade = {i['idade']}')
print('-'*30)