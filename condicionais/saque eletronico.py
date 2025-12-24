while True:
    saque = int(input('Qual o valor a ser sacado: R$'))
    total = 0
    sobra = saque

    
    notascinquenta = saque // 50
    if notascinquenta >= 1:
        print(f'Serão {int(notascinquenta)} notas de 50R$')
        total = total + (notascinquenta * 50)
        sobra = saque - total
        
    notasvinte = sobra // 20
    if notasvinte >= 1:
        print(f'Serão {int(notasvinte)} notas de 20R$')
        total = total + (notasvinte * 20)
        sobra = saque - total

    notasdez = sobra // 10
    if notasdez >= 1:
        print(f'Serão {int(notasdez)} notas de 10R$')
        total = total + (notasdez * 10)
        sobra = saque - total

    notasum = sobra // 1
    if notasum >= 1:
        print(f'Serão {int(notasum)} notas de 1R$')
        total += (notasum * 1)
    
    pergunta = input('Continua? [S/N]: ').upper()
    if pergunta == 'N':
        break





