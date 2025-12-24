


alunos = []
dados = []
while True:
    dados.append(str(input('Digite o nome do aluno: ')))
    dados.append(float(input('Digite a nota 1: ')))
    dados.append(float(input('Digite a nota 2: ')))
    alunos.append(dados[:])
    dados.clear()

    while True:
        resposta = input('Deseja continuar? [S/N]: ').upper()
        if resposta in 'SN':
            break
        else:
            print('Opção inválida.')
    if resposta == 'N':
        break
print('-'*30)

for posicao, valor_item in enumerate(alunos):
    media_aluno = (valor_item[1] + valor_item[2]) / 2
    print(f'Aluno {posicao}: {valor_item[0]} | Média = {media_aluno}')
print('-'*30)

while True:
    continuacao = int(input('Quer mostrar as notas de qual aluno? (999 interrompe): '))
    if continuacao == 999:
        break
    if continuacao > (len(alunos)-1) or continuacao <0:
        print('Aluno não encontrado')
    else:
        print(f'As notas de {alunos[continuacao][0]} foram {alunos[continuacao][1]}, {alunos[continuacao][2]}')
    
