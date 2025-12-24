n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Você foi reprovado! Obetve uma média de {media}.')
elif media > 7:
    print(f'Você foi aprovado! Obteve uma média de {media}.')
else:
    print(f'Você está de recuperação! Obteve uma média de {media}.')
    