n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

if n1 > n2 and n3:
    print (f'{n1} é o maior numero')
elif n2 > n1 and n3:
    print (f'{n2} é o maior número')
elif n3> n1 and n2:
    print(f'{n3} é o maior número')
 

if n1 < n2 and n3:
    print(f'{n1} é o menor numero')
elif n2 < n1 and n3:
    print(f'{n2} é o menor numero')
elif n3 < n1 and n2:
    print(f'{n3} é o menor numero')
