x = 0
while x != 5:
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    opcao = int(input("""Selecione a opção desejada:
                      [1] somar
                      [2] multiplicar
                      [3] maior
                      [4] novos números
                      [5] sair do programa 
                      """))
    x = opcao
    soma = v1 + v2
    mult = v1 * v2
    maior = max(v1,v2)
   
    if opcao == 1:
        print(f'a soma de {v1} e {v2} é {soma}')
    elif opcao == 2:
        print(f' A multiplicação de {v1} x {v2} é {mult}!')
    elif opcao == 3:
        print(f'O maior numero entre {v1} e {v2} é {maior}!')
    
