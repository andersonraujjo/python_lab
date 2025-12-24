


from datetime import datetime
ano_atual = datetime.now().year


dicionario = dict()


dicionario['nome'] = input('Qual o nome? ')
ano = int(input('Qual o ano de nascimento? '))
dicionario['idade'] = ano_atual - ano
dicionario['ctps'] = int(input('Tem carteira de trabalho? [0 não tem]: '))
if dicionario['ctps'] !=0:
    dicionario['anocontr'] = int(input('Ano de contratação: '))
    dicionario['salario'] = int(input('Salário: '))
    dicionario['aposentadoria'] = dicionario['anocontr'] + 35

print(dicionario)

for key, value in dicionario.items():
    print(f'{key} tem o valor {value}')


