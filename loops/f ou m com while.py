

while True:
    sexo = str(input('Digite o sexo: [F]/[M]: ')).upper()
    if sexo != 'F' and sexo != 'M':
        print('opção invalida')
    elif sexo == 'F' or sexo == 'M':
        break
  