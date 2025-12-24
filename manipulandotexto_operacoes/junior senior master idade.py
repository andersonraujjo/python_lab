born = int(input('Digite seu ano de nascimento: '))
anobase = 2024
idade = anobase - born
infantil = [10,11,12,13,14]
junior = [15,16,17,18,19]

if idade <= 9:
    print('Sua categoria de acordo com sua idade é a Mirim!')

if idade in infantil:
    print (f'Sua categoria de acordo com sua idade ({idade}) é a Infantil!')

if idade in junior:
    print(f'Sua categoria de acordo com sua idade ({idade}) é a Junior!')

if idade == 20:
    print(f'Sua categoria de acordo com sua idade ({idade}) é a Sênior!')

if idade >20:
    print(f'Sua categoria de acordo com sua idade ({idade}) é a Master!')

