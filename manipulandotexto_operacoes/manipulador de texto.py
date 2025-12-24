print('####################################################################################################################################################')
print ('\n')
print('Manipulador de texto, alterando tamanho e contagem de caracteres.')
print ('\n')

nome = input('Digite seu nome completo: ')
maius = nome.upper()
minus = nome.lower()
nse = nome.replace(' ', '')
qtdletr = len(nse)
div = nome.split()
qtdletr1 = len(div[0])




print(f'O nome em letra maiúscula é {maius}, em letras minúsculas é {minus}, a quantidade de letras no nome é {qtdletr}, e a quantidade de letras do primeiro nome é {qtdletr1}!')
