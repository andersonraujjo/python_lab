born = int(input('Digite o ano de seu nascimento: '))
anobase = 2024
idade = anobase - born
tempo = 18 - idade
tempo2 = idade - 18
if idade > 18:
    print(f'Você tinha que ter se alistado há {tempo2} ano(s) atrás!')
elif idade == 18:
    print('Você precisa se alistar urgentemente esse ano!')
elif idade < 18:
    print(f'Você ainda tem {tempo} ano(s) para se alistar, fique tranquilo!')
