
while True:
    try:
        inteiro = int(input('Digite um numero inteiro: '))
        break
    except (ValueError,TypeError):
        print('Erro, digite um numero inteiro válido.')

while True:
    try:
        real_validacao = input('Digite um numero real: ').lower()
        if real_validacao in ('inf','-inf','nan'):
            print('Erro: inf, -inf ou nan não são válidos.')
        elif real_validacao.isnumeric():
            print('Erro, você digitou um numero inteiro.')
        else:
            real_str = real_validacao.replace(',','.')
            real_str = real_str.strip()
            real = float(real_str)
            break
    except (ValueError,TypeError):
        print('Erro. Tipo de dado não suportado.')
    
    if not real_validacao:
        real = 0
        print('O usuario decidiu interromper o programa.')
        break

print(f'O numero inteiro digitado foi o {inteiro} e o real {real}.')