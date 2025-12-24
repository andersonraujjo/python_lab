n = int(input('Digite um número inteiro: ')) 
poss = int(input('Digite 1 para conversão em binário, 2 para octal, 3 para hexadecimal ou 4 para mostrar todos: '))
b = bin(n)
o = oct(n)
h = hex(n)

if poss == 1:
    print(f'O número {n} em binario é igual a {b}')
elif poss == 2:
    print(f'O número {n} em octal é igual a {o}')
elif poss == 3:
    print (f'O número {n} em hexadecima é igual a {h}')
elif poss ==4:
    print(f'O número {n} em binario é igual a {b}, em octal é igual a {o} e em hexadecimal é igual a {h}')
else:
    print('Número inválido!')