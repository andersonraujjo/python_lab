


def maior ():
    lista = []
    while True:
        numero_usuario = int(input('Digite um valor: '))
        lista.append(numero_usuario)
        while True:
            resposta_usuario = str(input('Deseja continuar? [S/N]: ')).upper()
            if resposta_usuario in 'SN':
                break
            print('Opção inválida')
        if resposta_usuario == 'N':
            break
    print('Analisando os valores informados..')
    for i in lista:
        print(i,end=' ')
    print(f'O maior valor informado foi o {max(lista)}')

maior()
    
resposta = str(input('Deseja continuar informando novos valores para análise? [S/N]: ')).upper()
if resposta == 'S':
    maior()
else:
    print('ATÉ LOGO')

