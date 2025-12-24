print('SEJA BEM VINDO AO HEALTHY4LIFE')

re1 = input('VAMOS COMEÇAR? (Digite sim ou não):') .lower

if re1 == 'não':
    print('QUE PENA1 QUEM SABE DA PRÓXIMA VEZ!')
else:
    print('RESPOSTA INVÁLIDA')

if re1 == 'sim':
    print('QUE ÓTIMO, VAMOS DAR INICIO ENTÃO!')
escolha = int(input(""" Preciso saber primeiro quais são seus objetivos com esse aplicativo. Digite o numero correspondente para cada alternativa.
          1 - Ganhar Peso
          2 - Perder Peso
          3 - Sair do sedentarismo
          4 - Ser mais saudável e melhorar níveis de estresse e ansiedade
          Qual sua escolha?: """))
if escolha == 1 and 2:
    altura = float(input('Preciso dos alguns dados seus. Qual sua altura?: '))
    peso = float(input('Digite o seu peso atual: '))
    imc = peso / (altura * altura)
    if imc <18.25:
        print('Você está abaixo do peso recomendado! Recomenda-se comer mais e de maneira limpa para atingir o peso ideal.')
    elif imc >18.25 and imc <=25:
        print('Você está no peso ideal!')
    elif imc >25 and imc <=30:
        print('Você está com sobrepeso! Deve maneirar na comida ou aumentar a atividade física.')
    elif imc >30 and imc <=40:
        print('Você está com obesidade! Precisamos dar um jeito nessa situação pra ontem!.')
    else:
        print('Você está com obesidade mórbida! O ideal seria procurar ajuda profissional!.')

elif escolha == 3:
    arquivo =  open("teste.txt" "r")
    conteudo = arquivo.read()
    print(conteudo)