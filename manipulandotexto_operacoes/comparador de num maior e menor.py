n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior que o segundo ({n2})!')
elif n2 > n1:
    print(f'O segundo valor ({n2}) é maior que o primeiro ({n1})!')
else:
    print(f'Nenhum valor é maior que o outro! Ambos são iguais ({n1}) e ({n2})!')