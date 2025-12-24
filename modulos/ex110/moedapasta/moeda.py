


def cifrao(preco):
    preco_str = str(preco)
    preco_str_form = preco_str.replace('.',',')
    preco_str_form = 'R$' + preco_str_form
    return preco_str_form
    #return f'R${preco:.2f}'.replace('.', ',')


def metade(preco):
    resp = preco / 2
    return cifrao(resp)

def dobro(preco):
    resp = preco * 2
    return cifrao(resp)

def aumentar(preco,b):
    por_cen = b / 100
    aum = por_cen * preco
    resp = preco + aum
    return cifrao(resp)

def diminuir(preco,b):
    por_cent = b / 100
    dim = por_cent * preco
    resp = preco - dim
    return cifrao(resp)


def leiaDinheiro(msg):

    while True:
        preco = input(msg)
        if ',' in preco:
            preco = preco.replace(',','.')
            preco = float(preco)
            break
        elif '.' in preco:
            preco = float(preco)
            break
        elif preco.isnumeric():
            preco = float(preco)
            break
        else:
            print('ERRO, digite um número válido.')
    return preco



def resumo(preco,a,b):
    print('-'*30)
    print(f'{'RESUMO DO VALOR:':^25}')
    print('-'*30)
    print(f'Preço analisado:{cifrao(preco):>10}')
    print(f'Dobro do preço: {dobro(preco):>10}')
    print(f'Metade do preço:{metade(preco):>10}')
    print(f'{a}% de aumento: {aumentar(preco,a):>10}')
    print(f'{b}% de redução: {diminuir(preco,b):>10}')
    print('-'*30)