



primeiro_numero = int(input('Digite um numero: '))
segundo_numero = int(input('Digite um numero: '))
terceiro_numero = int(input('Digite um numero: '))
quarto_numero = int(input('Digite um numero: '))

tuplinha_dos_crias = (primeiro_numero,segundo_numero,terceiro_numero,quarto_numero)

if tuplinha_dos_crias.count(9) >=1:
    print(f'O numero 9 foi digitado {tuplinha_dos_crias.count(9)} vezes!')
else:
    print('O numero 9 não foi digitado nenhuma vez')

if tuplinha_dos_crias.count(3) >=1:
    print(f'O numero 3 foi digitado a primeira vez na posição {tuplinha_dos_crias.index(3)+1}')
else:
    print('O numero 3 não foi digitado nenhuma vez.')

print('Os pares digitados foram: ', end=' ')
for i in tuplinha_dos_crias:
    if i %2 == 0:
        print(i, end=' ')
   
    


