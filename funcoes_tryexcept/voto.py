

from datetime import date
data = date.today()

def voto (idade):
    if idade > 18 and idade < 65:
        return 'OBRIGATÓRIO'
    elif idade < 18:
        return 'PROIBIDO'
    else:
        return 'OPCIONAL'

ano = int(input('Qual o ano de nascimento? '))
idade = data.year - ano

print(f'Com {idade} anos: O voto é {voto()}')