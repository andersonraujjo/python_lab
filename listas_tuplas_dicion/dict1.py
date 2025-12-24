


dicionario_media = {}

dicionario_media['nome'] = input('Qual o nome do aluno? ')
dicionario_media['media'] = float(input('Qual a média do aluno? '))
if dicionario_media['media'] > 7:
    dicionario_media['situação'] = 'Aprovado'
else:
    dicionario_media['situação'] = 'Reprovado'

print(f'O nome é {dicionario_media["nome"]}, a média é {dicionario_media["media"]} e a situação é: {dicionario_media["situação"]}')

#ou com laço for
for k, v in dicionario_media.items():
    print(k,v)

