n1 = 0
n2 = 0
n1e2 = 0
r = 0

while r != 4 and 5:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    if n1 > n2:
        n1e2 = n1e2 + n1
    else:
        n1e2 = n1e2 + n2
    i = int(input("""O que você quer fazer com esses dois números digitados?
    1 = soma
    2 = mult
    3 = maior
    4 = novos num
    5 = sair
    = """))
    if i == 1:
        soma = n1 + n2
        print(f'A soma dos números {n1} e {n2} é igual a {soma}!')
    elif i == 2:
        mult = n1 * n2
        print(f'A multiplicação dos numeros {n1} e {n2} é igual a {mult}!')
    elif i == 3:
        print(f'O maior numero entre {n1} e {n2} é o {n1e2}!')
    elif i == 5:
        break
