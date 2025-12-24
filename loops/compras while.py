

totalgasto = 0
produtoscaros = 0
produtobarato = float('inf')
nomeprodutobarato = ''
primeiroproduto = True


while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    totalgasto += preco

    if primeiroproduto:
        nomeprodutobarato = nome
        produtobarato = preco
        primeiroproduto = False

    while True:
        escolha = input('Deseja continuar a compra? [S/N]: ').upper()
        if escolha not in ('S','N'):
            print('Opção invalida')
        else:
            break


    if preco < produtobarato:
        produtobarato = preco
        nomeprodutobarato = nome

    if preco > 1000:
        produtoscaros += 1

    if escolha == 'N':
        break



print(f'O total gasto com a compra foi de {totalgasto} reais!')

if produtoscaros >0:
    print(f'Na sua compra tem {produtoscaros} produtos que custam mais de 1000 reais!')
else:
    print('Nenhum produto acima de 1000 reais.')

print(f'A compra mais barata foi o/a {nomeprodutobarato}!')
