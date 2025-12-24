
mais20 = 0
listahomens = 0
menos20 = 0

while True:
    idade = int(input('Digite a idade: ')) 
    
    while True:
        sexo = input('Digite o sexo [F/M]: ').upper()
        if sexo not in ('F','M'):
            print('Opção invalida!')
        else:
            break
   
    if idade > 20:
        mais20 += 1
    if sexo == 'M':
        listahomens += 1
    if sexo == 'F' and idade <20:
        menos20 += 1

    
    while True: 
        escolha = input('Deseja continuar cadastrando? [S/N]: ').upper()
        if escolha not in ('S','N'):
            print('Opção inválida!')

        else:
            break

    if escolha == 'N':
        break

    

if mais20 ==0:
    print('Nenhuma pessoas com mais de 20 anos cadastrada.')
else:
    print(f'Ao todo são {mais20} pessoas com mais de 20 anos.')


if listahomens == 0:
    print('Nenhum homem foi cadastrado na lista.')
else:
    print(f'Ao todo foram cadastrados {listahomens} homens!')


if menos20 == 0:
    print('Nenhuma mulher com menos de 20 anos cadastrada.')
else:
    print(f'Ao todo foram cadastradas {menos20} mulheres com menos de 20 anos!')