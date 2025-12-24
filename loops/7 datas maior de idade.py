listamaiores = 0
for i in range (1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = 2024 - nasc
    if idade >= 21:
        listamaiores = listamaiores + 1
print(f'Das 07 pessoas, {listamaiores} são maiores de idade!')
