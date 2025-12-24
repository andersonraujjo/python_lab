


expressao_usuario = input('Digite a sua expressão: ')

contador_abre = 0
contador_fecha = 0

for i in expressao_usuario:
    if i == '(':
        contador_abre += 1
    if i == ')':
        contador_fecha += 1

if contador_abre == contador_fecha:
    print('Sua expressão está correta!')
else:
    print(f'A expressão {expressao_usuario} está incorreta!')