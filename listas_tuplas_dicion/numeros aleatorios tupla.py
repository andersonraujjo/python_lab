


from random import randint



while True: 
    lista_dos_numeros = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
    print(lista_dos_numeros)
    print(f'O maior valor é o {max(lista_dos_numeros)} e o menor é o {min(lista_dos_numeros)}')
    
    while True:
        resposta = input('Continua? [S/N]: ').upper()
        if resposta not in 'SN':
            print('Opção invalida')
        if resposta in 'SN':
            break
    if resposta == 'N':
        break







