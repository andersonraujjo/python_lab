peso = float(input('Digite o seu peso atual: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)

print(f'Seu imc é de {imc:.1f}')

if imc <18.25:
    print('Você está abaixo do peso recomendado!')
elif imc >18.25 and imc <=25:
    print('Você está no peso ideal!')
elif imc >25 and imc <=30:
    print('Você está com sobrepeso! Pare de comer gorducho.')
elif imc >30 and imc <=40:
    print('Você está com obesidade! Projeto baleia vem aí.')
else:
    print('Você está com obesidade mórbida! Larga esse cookie agora, u fat fuck.')