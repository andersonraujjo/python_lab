sal = int(input('Digite o seu salário: '))
s10 = sal * 0.10
s15 = sal * 0.15
s10r = s10 + sal
s15r = s15 + sal
if sal > 1250:
    print(f'O salario com aumento vai ser de {s10r})')
elif sal < 1250:
    print(f'O salario com aumento de 15% será de {s15r}')
    